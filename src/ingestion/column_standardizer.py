# Imagine we receive data from different companies.

# File 1
# Claim ID
# Customer Name
# Claim Amount

# File 2
# claim_id
# customer_name
# claim_amount

# File 3
# CLAIM-ID
# CUSTOMER NAME
# CLAIM_AMOUNT

# If we don't standardize them, our code will constantly break because it expects consistent column names.

# So we'll convert all of them into:

# claim_id
# customer_name
# claim_amount

# This is a very common ETL task in production pipelines.

import re
import pandas as pd


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names:
    - Lowercase
    - Replace spaces and special characters with underscores
    - Remove leading/trailing underscores
    """

    df.columns = [
        re.sub(r"[^a-zA-Z0-9]+", "_", column.strip().lower()).strip("_")
        for column in df.columns
    ]

    return df

