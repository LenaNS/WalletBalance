import uuid

from sqlalchemy.dialects.postgresql import UUID, INTEGER
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.models.base import Base


class Wallet(Base):
    """
    Модель кошелька.

    Поля
    ----
    __tablename__: str
        Имя таблицы в базе данных.
    id: UUID
        Уникальный идентификатор кошелька.
    balance: int
        Баланс кошелька.
    """
    __tablename__ = 'wallets'

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4())
    balance: Mapped[int] = mapped_column(INTEGER, default=0)
