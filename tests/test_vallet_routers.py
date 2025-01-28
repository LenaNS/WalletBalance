import asyncio
import random
import uuid

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from src.app import api_app
from src.db.db import async_session
from src.models.wallets import Wallet


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=api_app), base_url="http://test") as client:
        yield client


@pytest_asyncio.fixture(scope="function")
async def create_wallet():
    async with async_session() as session:
        instance = Wallet(id=uuid.uuid4(), balance=random.randint(100, 10000))
        print(instance.balance)
        session.add(instance)
        await session.commit()
        yield instance


@pytest_asyncio.fixture(scope="function")
async def create_fake_wallet_uuid():
    wallet_uuid = uuid.uuid4()

    async with async_session() as session:
        while True:
            instance = await session.get(Wallet, wallet_uuid)
            if instance:
                wallet_uuid = uuid.uuid4()
            else:
                break
        yield wallet_uuid


@pytest.mark.asyncio
async def test_get_balance(async_client, create_wallet):
    wallet_uuid = create_wallet.id
    response = await async_client.get(f"api/v1/wallets/{wallet_uuid}")
    result = response.json()

    assert response.status_code == 200
    assert result['balance'] == create_wallet.balance


@pytest.mark.asyncio
async def test_get_balance_error(async_client, create_fake_wallet_uuid):
    response = await async_client.get(f"api/v1/wallets/{create_fake_wallet_uuid}")
    result = response.json()

    assert response.status_code == 404
    assert result['detail'] == 'Кошелёк не найден. Проверьте uuid.'


@pytest.mark.asyncio
async def test_deposit(async_client, create_wallet):
    wallet_uuid = create_wallet.id
    data = {
        "amount": 50,
        "operation_type": "DEPOSIT"
    }
    response = await async_client.post(f"api/v1/wallets/{wallet_uuid}/operation", json=data)
    result = response.json()

    balance = create_wallet.balance + data['amount']

    assert response.status_code == 200
    assert result['balance'] == balance


@pytest.mark.asyncio
async def test_successful_withdraw(async_client, create_wallet):
    wallet_uuid = create_wallet.id
    data = {
        "amount": 50,
        "operation_type": "WITHDRAW"
    }
    response = await async_client.post(f"api/v1/wallets/{wallet_uuid}/operation", json=data)
    result = response.json()

    balance = create_wallet.balance - data['amount']

    assert response.status_code == 200
    assert result['balance'] == balance


@pytest.mark.asyncio
async def test_unsuccessful_withdraw(async_client, create_wallet):
    wallet_uuid = create_wallet.id
    data = {
        "amount": create_wallet.balance + 1,
        "operation_type": "WITHDRAW"
    }
    response = await async_client.post(f"api/v1/wallets/{wallet_uuid}/operation", json=data)
    result = response.json()

    balance = create_wallet.balance - data['amount']

    assert response.status_code == 400
    assert result['detail'] == 'Сумма списания больше, чем баланс кошелька.'


@pytest.mark.asyncio
async def test_negative_amount_operation(async_client, create_wallet):
    wallet_uuid = create_wallet.id
    data = {
        "amount": -1,
        "operation_type": "WITHDRAW"
    }
    response = await async_client.post(f"api/v1/wallets/{wallet_uuid}/operation", json=data)
    result = response.json()

    assert response.status_code == 422
    assert result['detail'] == 'Ошибка валидации. Проверьте введённые значения.'
