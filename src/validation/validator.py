import pandas as pd

from src.validation.rules import (
    validate_required_fields,
    validate_claim_amount,
    validate_claim_date
)

from src.utils.logger import get_logger


logger = get_logger(__name__)


class Validator:
    """
    Applies validation rules to claim data.
    """

    def validate(self, df: pd.DataFrame):

        logger.info("Starting data validation")

        valid_records = []
        rejected_records = []

        for _, row in df.iterrows():

            record = row.to_dict()

            errors = []

            errors.extend(
                validate_required_fields(record)
            )

            errors.extend(
                validate_claim_amount(record)
            )

            errors.extend(
                validate_claim_date(record)
            )

            if errors:
                record["validation_errors"] = errors
                rejected_records.append(record)

            else:
                valid_records.append(record)

        valid_df = pd.DataFrame(valid_records)
        rejected_df = pd.DataFrame(rejected_records)

        logger.info(
            f"Validation completed. "
            f"Valid: {len(valid_df)}, "
            f"Rejected: {len(rejected_df)}"
        )

        return valid_df, rejected_df