import sqlite3
from pathlib import Path

from src.utils.logger import get_logger


logger = get_logger(__name__)


DATABASE_PATH = "data/warehouse/claims.db"


def get_connection():

    database_file = Path(DATABASE_PATH)

    # create folder automatically
    database_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    logger.info(
        "Creating warehouse database connection"
    )

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    return connection