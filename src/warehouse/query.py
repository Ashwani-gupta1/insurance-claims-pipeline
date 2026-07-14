import pandas as pd

from src.warehouse.database import get_connection


def get_all_claims():

    conn = get_connection()

    df = pd.read_sql(
        "SELECT * FROM claims_fact",
        conn
    )

    conn.close()

    return df