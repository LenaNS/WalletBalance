import logging

import uvicorn

from src.app import api_app
from src.db.migrations import run_migrations

if __name__ == "__main__":
    try:
        run_migrations()

    except RuntimeError as ignored:
        logging.log(0, ignored)

    uvicorn.run(app="main:api_app", host="0.0.0.0", port=8000, workers=4)
