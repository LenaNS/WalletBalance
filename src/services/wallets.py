from uuid import UUID

from src.models.wallets import Wallet
from src.repositories.wallets import WalletRepository
from src.schemas.wallets import WalletSchema, OperationSchema, OperationType


class WalletService:
    """
    Сервис для работы с кошельками.

    Поля
    ----
     repository : WalletRepository
        Репозиторий для работы с кошельками.
    """

    def __init__(self, repository: WalletRepository):
        self.repository: WalletRepository = repository

    async def get_balance(self, wallet_uuid: UUID) -> Wallet | None:
        """
        Получает информацию о балансе кошелька по его UUID.

        :param wallet_uuid: UUID кошелька.
        :return: Экземпляр Wallet или None, если кошелька не существует.
        """
        instance = await self.repository.get(uuid=wallet_uuid)
        return instance

    async def do_operation(self, wallet_uuid: UUID, data: OperationSchema) -> Wallet:
        """
        Выполняет операцию с кошельком (начисление или снятие средств).

        :param wallet_uuid: UUID кошелька.
        :param data: Данные, содержащие информацию о типе операции и сумме начисления/списания.
        :return: Обновлённый экземпляр Wallet.
        """
        amount = data.amount if data.operation_type is OperationType.deposit else -data.amount
        instance = await self.repository.update(wallet_uuid, amount)
        return instance
