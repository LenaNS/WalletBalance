from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.api.routers import api_router

from src.exceptions.exception import *


api_app = FastAPI()

api_app.include_router(router=api_router)


@api_app.exception_handler(WalletError)
async def wallet_error_handler(request: Request, exc: WalletError):
    """
    Обработчик всех ошибок типа WalletError.
    :param request: Запрос, вызвавший ошибку.
    :param exc: Исключение типа WalletError, содержащее информацию об ошибке.
    :return: JSON с кодом ошибки и сообщением
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@api_app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Обработчик ошибок валидации запросов.
    :param request: Запрос, вызвавший ошибку.
    :param exc: Исключение типа RequestValidationError, содержащее информацию ошибки валидации.
    :return: JSON с кодом ошибки и сообщением
    """
    return JSONResponse(
        status_code=422,
        content={"detail": "Ошибка валидации. Проверьте введённые значения."}
    )