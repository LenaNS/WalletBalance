from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends

from src.api.v1.dependencies import wallets_service
from src.exceptions.exception import WalletNotFoundError
from src.schemas.wallets import OperationSchema

from src.services.wallets import WalletService

wallet_router = APIRouter(
    prefix="/wallets"
)


@wallet_router.get("/{wallet_uuid}")
async def get_balance(wallet_uuid: UUID,
                      service: Annotated[WalletService, Depends(wallets_service)]):
    """
    Маршрут получения баланса по UUID.

    :param wallet_uuid: UUID кошелька.

    :param service: Сервис работы с кошельками.

    :return: Возвращает текущий баланс кошелька при успешном выполнении запроса. Если кошелек не найден возвращает 404.
    """
    balance = await service.get_balance(wallet_uuid=wallet_uuid)
    if not balance:
        raise WalletNotFoundError
    return balance
    # return {"balance": balance}


@wallet_router.post("/{wallet_uuid}/operation")
async def do_operation(wallet_uuid: UUID,
                       data: OperationSchema,
                       service: Annotated[WalletService, Depends(wallets_service)]):
    """
    Маршрут выполнения операции начисления/списания.

    :param **wallet_uuid**: UUID кошелька.

    :param **data**: Входные данные.

    :param **service**: Сервис работы с кошельками.

    :return: Возвращает текущий баланс кошелька при успешном выполнении запроса (200).
             При некорректном запросе возвращает текст ошибки с кодом ответа: 422 при ошибках валидации,
             404 если кошелек не найден, 400 если на балансе не достаточно средств.
    """
    operation_result = await service.do_operation(wallet_uuid=wallet_uuid, data=data)
    if not operation_result:
        raise WalletNotFoundError
    return operation_result
