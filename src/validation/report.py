from src.utils.logger import get_logger


logger = get_logger(__name__)


class ValidationReport:

    def generate(self, total_records, valid_df, rejected_df):

        report = {
            "total_records": total_records,
            "valid_records": len(valid_df),
            "rejected_records": len(rejected_df),
            "rejection_rate": round(
                (len(rejected_df) / total_records) * 100,
                2
            ) if total_records > 0 else 0
        }

        logger.info(
            f"Validation Report: {report}"
        )

        return report