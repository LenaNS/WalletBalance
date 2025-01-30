from uuid import UUID

from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select


from src.db.db import async_session
from src.exceptions.exception import WalletOperationError
from src.models.wallets import Wallet


class WalletRepository:
    """
    Репозиторий для работы с кошельками.

    Поля
    ----
    model: Wallet
        Модель кошелька, используемая для взаимодействия с базой данных.
    """

    model = Wallet

    async def get(self, uuid: UUID) -> Wallet | None:
        """
        Получает кошелёк по UUID.

        :param uuid: UUID кошелька.
        :return: Экземпляр Wallet или None, если кошелька не существует.
        """
        async with async_session() as session:
            instance = await session.get(self.model, uuid)
            return instance

    async def update(self, uuid: UUID, amount: int) -> Wallet | None:
        """
        Обновляет баланс кошелька.

        :param uuid: UUID кошелька.
        :param amount: Сумма на которую изменяется баланс кошелька.
        :return: Экземпляр Wallet или None, если кошелька не существует.
        """
        async with async_session() as session:
            async with session.begin():
                instance = await session.execute(
                    select(self.model).where(self.model.id == uuid).with_for_update()
                )
                instance = instance.scalar()
                # instance = await session.get(self.model, uuid)
                if instance:
                    instance.balance += amount
                    try:
                        await session.commit()
                        return instance
                    except IntegrityError as ex:
                        raise WalletOperationError

        return None
