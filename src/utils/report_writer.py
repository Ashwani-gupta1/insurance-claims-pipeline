import json
from pathlib import Path

from src.utils.logger import get_logger


logger = get_logger(__name__)


class ReportWriter:

    def write_json(self, report, output_path):

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(path, "w") as file:
            json.dump(
                report,
                file,
                indent=4
            )

        logger.info(
            f"Validation report written to {output_path}"
        )