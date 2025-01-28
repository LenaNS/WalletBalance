class WalletError(Exception):
    """
    Основной класс ошибок кошельков.
    """

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)


class WalletNotFoundError(WalletError):
    """
    Класс ошибок 404 для кошельков.
    """

    def __init__(self):
        super().__init__(status_code=404, message='Кошелёк не найден. Проверьте uuid.')


class WalletOperationError(WalletError):
    """
    Класс ошибок некорректных операций.
    """

    def __init__(self):
        super().__init__(status_code=400, message='Сумма списания больше, чем баланс кошелька.')
