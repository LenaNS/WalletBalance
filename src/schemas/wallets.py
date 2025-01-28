from enum import Enum
from uuid import UUID

from pydantic import BaseModel, Field


class WalletSchema(BaseModel):
    """
    Схема отображения баланса.

    Поля
    ----
    **id**: UUID
        UUID кошелька.

    **balance**: int
        баланс кошелька.
    """
    id: UUID
    balance: int


class OperationType(str, Enum):
    """
    Перечисление типов операций.

    Поля
    ----
    **deposit**: str
        Операция пополнения.

    **withdraw**: str
        Операция списания.
    """
    deposit = 'DEPOSIT'
    withdraw = 'WITHDRAW'


class OperationSchema(BaseModel):
    """
    Схема данных для проведения операции.

    Поля
    ----
    **operation_type**: OperationType
        Тип операции.

    **amount**: int
        Сумма начисления/списания с ограничением больше 0.
    """
    operation_type: OperationType
    amount: int = Field(gt=0)
