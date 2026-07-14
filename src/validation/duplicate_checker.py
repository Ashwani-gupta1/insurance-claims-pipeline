from src.utils.logger import get_logger


logger = get_logger(__name__)


class DuplicateChecker:
    """
    Detect duplicate insurance claims.
    """

    def check(self, df):

        logger.info("Checking duplicate claims")

        duplicate_mask = df.duplicated(
            subset=["claim_id"],
            keep=False
        )

        duplicates = df[duplicate_mask]

        clean_records = df[
            ~duplicate_mask
        ]

        logger.info(
            f"Duplicate records found: {len(duplicates)}"
        )

        return clean_records, duplicates