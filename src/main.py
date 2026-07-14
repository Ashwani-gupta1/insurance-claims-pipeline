from src.ingestion.reader import DataReader

from src.validation.validator import Validator
from src.validation.duplicate_checker import DuplicateChecker
from src.validation.report import ValidationReport

from src.transform.claim_transformer import ClaimTransformer

from src.utils.writer import DataWriter
from src.utils.report_writer import ReportWriter
from src.utils.logger import get_logger


logger = get_logger(__name__)


def main():

    file_path = "data/sample/claims.csv"

    try:

        logger.info("Starting claims pipeline")


        # -------------------------
        # Step 1: Ingestion
        # -------------------------
        reader = DataReader()

        df = reader.read(file_path)

        logger.info(
            f"Records received: {len(df)}"
        )


        # -------------------------
        # Step 2: Validation
        # -------------------------
        validator = Validator()

        valid_df, rejected_df = validator.validate(df)



        # -------------------------
        # Step 3: Duplicate Detection
        # -------------------------
        duplicate_checker = DuplicateChecker()

        clean_df, duplicate_df = duplicate_checker.check(
            valid_df
        )


        if not duplicate_df.empty:

            duplicate_df["validation_errors"] = (
                "Duplicate claim_id"
            )

            import pandas as pd

            rejected_df = pd.concat(
                [
                    rejected_df,
                    duplicate_df
                ],
                ignore_index=True
            )


        # -------------------------
        # Step 4: Transformation
        # -------------------------
        transformer = ClaimTransformer()

        transformed_df = transformer.transform(
            clean_df
        )


        # -------------------------
        # Step 5: Write Output Files
        # -------------------------
        writer = DataWriter()


        writer.write_csv(
            transformed_df,
            "data/processed/valid_claims.csv"
        )


        writer.write_csv(
            rejected_df,
            "data/rejected/rejected_claims.csv"
        )


        # -------------------------
        # Step 6: Generate Report
        # -------------------------
        report_generator = ValidationReport()

        report = report_generator.generate(
            len(df),
            transformed_df,
            rejected_df
        )


        # -------------------------
        # Step 7: Save Report JSON
        # -------------------------
        report_writer = ReportWriter()

        report_writer.write_json(
            report,
            "data/reports/validation_report.json"
        )


        # -------------------------
        # Console Output
        # -------------------------
        print("\nPROCESSED CLAIMS")
        print("----------------")
        print(transformed_df)


        print("\nREJECTED CLAIMS")
        print("----------------")
        print(rejected_df)


        print("\nVALIDATION REPORT")
        print("----------------")
        print(report)



    except Exception as e:

        logger.error(
            f"Pipeline failed: {str(e)}"
        )

        raise



if __name__ == "__main__":
    main()