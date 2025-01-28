from fastapi import APIRouter

from src.api.v1.wallets import wallet_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(router=wallet_router)
