from pathlib import Path
import pandas as pd

from src.utils.logger import get_logger


logger = get_logger(__name__)


class DataWriter:

    def write_csv(self, df, output_path):

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_csv(
            path,
            index=False
        )

        logger.info(
            f"Written {len(df)} records to {output_path}"
        )