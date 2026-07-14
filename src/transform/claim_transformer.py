import pandas as pd

from src.transform.business_rules import (
    classify_claim_amount,
    assign_priority
)

from src.utils.logger import get_logger


logger = get_logger(__name__)


class ClaimTransformer:
    """
    Apply business transformations on validated claims.
    """


    def transform(self, df):

        logger.info(
            "Starting claim transformation"
        )


        transformed_df = df.copy()


        # Add claim category
        transformed_df["claim_category"] = (
            transformed_df["claim_amount"]
            .apply(classify_claim_amount)
        )


        # Add priority
        transformed_df["priority"] = (
            transformed_df.apply(
                lambda row: assign_priority(
                    row["status"],
                    row["claim_amount"]
                ),
                axis=1
            )
        )


        # Add processing date
        transformed_df["processed_date"] = (
            pd.Timestamp.now()
            .date()
        )


        logger.info(
            "Claim transformation completed"
        )


        return transformed_df