from src.ai.client import AIClient
from src.ai.prompts import WAREHOUSE_SCHEMA
from src.utils.logger import get_logger


logger = get_logger(__name__)


class SQLGenerator:
    """
    Converts natural language questions into SQL.
    """

    def __init__(self):
        self.ai = AIClient()

    def generate(self, question: str) -> str:

        prompt = f"""
{WAREHOUSE_SCHEMA}

User Question:
{question}

Generate ONLY valid SQLite SQL.

Do not explain anything.

Only return SQL.
"""

        logger.info("Generating SQL using AI")

        sql = self.ai.ask(prompt)

        logger.info("SQL generated successfully")

        return sql.strip()