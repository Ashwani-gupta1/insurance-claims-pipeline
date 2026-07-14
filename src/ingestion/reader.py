from pathlib import Path

import pandas as pd

from src.ingestion.file_detector import get_file_extension
from src.ingestion.column_standardizer import standardize_columns
from src.utils.logger import get_logger


logger = get_logger(__name__)


class DataReader:
    """
    Reads different file formats and returns
    standardized pandas DataFrames.
    """

    def read(self, file_path: str) -> pd.DataFrame:

        logger.info(f"Reading file: {file_path}")

        path = Path(file_path)

        if not path.exists():
            logger.error(f"File not found: {file_path}")
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        extension = get_file_extension(file_path)

        logger.info(f"Detected file type: {extension}")

        if extension == ".csv":
            df = pd.read_csv(file_path)

        elif extension in [".xlsx", ".xls"]:
            df = pd.read_excel(file_path)

        elif extension == ".json":
            df = pd.read_json(file_path)

        else:
            logger.error(
                f"Unsupported file format: {extension}"
            )
            raise ValueError(
                f"Unsupported file format: {extension}"
            )

        logger.info(
            f"Records loaded: {len(df)}"
        )

        df = standardize_columns(df)

        logger.info(
            f"Columns standardized: {df.columns.tolist()}"
        )

        return df