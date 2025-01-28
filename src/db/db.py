import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(f'postgresql+asyncpg://{os.getenv("USERNAME", "postgres")}:{os.getenv("PASSWORD", "admin")}@{os.getenv("HOST", "localhost")}/{os.getenv("DB", "DBWalletBalance")}')

async_session = async_sessionmaker(engine, expire_on_commit=False)
