from src.repositories.wallets import WalletRepository
from src.services.wallets import WalletService


def wallets_service() -> WalletService:
    """
    Конструирует экземпляр сервиса для работы с кошельками.

    :return: Сервис для работы с кошельками.
    """
    return WalletService(WalletRepository())
