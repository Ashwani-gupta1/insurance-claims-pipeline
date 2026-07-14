import pandas as pd

from src.analytics.queries import execute_query


class ClaimMetrics:

    def get_total_claims(self):
        columns, rows = execute_query("""
            SELECT COUNT(*) AS total_claims
            FROM claims_fact
        """)

        return pd.DataFrame(rows, columns=columns)

    def get_total_claim_amount(self):
        columns, rows = execute_query("""
            SELECT SUM(claim_amount) AS total_claim_amount
            FROM claims_fact
        """)

        return pd.DataFrame(rows, columns=columns)

    def get_average_claim_amount(self):
        columns, rows = execute_query("""
            SELECT ROUND(AVG(claim_amount),2) AS average_claim_amount
            FROM claims_fact
        """)

        return pd.DataFrame(rows, columns=columns)

    def get_claims_by_status(self):
        columns, rows = execute_query("""
            SELECT
                status,
                COUNT(*) AS total_claims
            FROM claims_fact
            GROUP BY status
            ORDER BY total_claims DESC
        """)

        return pd.DataFrame(rows, columns=columns)

    def get_claims_by_priority(self):
        columns, rows = execute_query("""
            SELECT
                priority,
                COUNT(*) AS total_claims
            FROM claims_fact
            GROUP BY priority
            ORDER BY total_claims DESC
        """)

        return pd.DataFrame(rows, columns=columns)

    def get_top_5_claims(self):
        columns, rows = execute_query("""
            SELECT
                claim_id,
                customer_name,
                claim_amount
            FROM claims_fact
            ORDER BY claim_amount DESC
            LIMIT 5
        """)

        return pd.DataFrame(rows, columns=columns)