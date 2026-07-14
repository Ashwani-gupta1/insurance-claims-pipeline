from datetime import datetime

from src.warehouse.database import get_connection
from src.utils.logger import get_logger


logger = get_logger(__name__)


class WarehouseLoader:

    def load_claims(self, df):

        logger.info("Starting warehouse UPSERT")

        conn = get_connection()

        cursor = conn.cursor()

        upsert_sql = """
        INSERT INTO claims_fact
        (
            claim_id,
            customer_name,
            claim_amount,
            claim_date,
            status,
            claim_category,
            priority,
            processed_date,
            created_at,
            updated_at
        )
        VALUES
        (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )

        ON CONFLICT(claim_id)

        DO UPDATE SET

            customer_name = excluded.customer_name,
            claim_amount = excluded.claim_amount,
            claim_date = excluded.claim_date,
            status = excluded.status,
            claim_category = excluded.claim_category,
            priority = excluded.priority,
            processed_date = excluded.processed_date,
            updated_at = excluded.updated_at;
        """

        now = datetime.now().isoformat()

        records = []

        for _, row in df.iterrows():

            records.append(
                (
                    int(row["claim_id"]),
                    row["customer_name"],
                    float(row["claim_amount"]),
                    str(row["claim_date"]),
                    row["status"],
                    row["claim_category"],
                    row["priority"],
                    str(row["processed_date"]),
                    now,
                    now
                )
            )

        cursor.executemany(
            upsert_sql,
            records
        )

        conn.commit()

        conn.close()

        logger.info(
            f"{len(records)} records merged successfully"
        )