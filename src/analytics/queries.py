from src.warehouse.database import get_connection
from src.utils.logger import get_logger

logger = get_logger(__name__)


def execute_query(query):
    """
    Execute any SQL query and return the result.
    """

    logger.info("Executing SQL query")

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = [column[0] for column in cursor.description]

    conn.close()

    logger.info(f"Returned {len(rows)} rows")

    return columns, rows