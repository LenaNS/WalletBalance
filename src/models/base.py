from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Базовый класс моделей базы данных.

    Поля
    ----
    __abstract__: bool
        Указывает, что класс является абстрактным и не будет создан в базе данных.
    """
    __abstract__ = True
