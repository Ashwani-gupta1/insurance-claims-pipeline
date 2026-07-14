from src.warehouse.database import get_connection
from src.utils.logger import get_logger

logger = get_logger(__name__)


def create_tables():
    """
    Creates the warehouse tables if they do not already exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS claims_fact (

            claim_id INTEGER PRIMARY KEY,

            customer_name TEXT NOT NULL,

            claim_amount REAL NOT NULL,

            claim_date TEXT NOT NULL,

            status TEXT NOT NULL,

            claim_category TEXT,

            priority TEXT,

            processed_date TEXT,

            created_at TEXT,

            updated_at TEXT
        )
    """)

    conn.commit()
    conn.close()

    logger.info("claims_fact table created successfully")


if __name__ == "__main__":
    create_tables()