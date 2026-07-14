from src.ingestion.reader import DataReader
from src.utils.logger import get_logger


logger = get_logger(__name__)


def main():
    file_path = "data/sample/claims.csv"

    try:
        logger.info("Starting ingestion pipeline")

        reader = DataReader()

        df = reader.read(file_path)

        logger.info("Ingestion completed successfully")
        logger.info(f"Records loaded: {len(df)}")
        logger.info(f"Columns detected: {df.columns.tolist()}")

        print(df.head())

    except Exception as e:
        logger.error(f"Ingestion failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()