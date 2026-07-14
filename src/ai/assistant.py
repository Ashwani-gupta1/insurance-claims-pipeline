import pandas as pd

from src.ai.sql_generator import SQLGenerator
from src.analytics.queries import execute_query
from src.ai.client import AIClient
from src.utils.logger import get_logger


logger = get_logger(__name__)


class AIAssistant:

    def __init__(self):

        self.sql_generator = SQLGenerator()
        self.ai = AIClient()

    def ask(self, question: str) -> pd.DataFrame:
        """
        Convert natural language to SQL,
        execute it,
        and return a DataFrame.
        """

        logger.info(f"Question: {question}")

        # Generate SQL
        sql = self.sql_generator.generate(question)

        logger.info(f"Generated SQL:\n{sql}")

        # Execute SQL
        columns, rows = execute_query(sql)

        # Convert to DataFrame
        df = pd.DataFrame(
            rows,
            columns=columns
        )

        return df

    def explain(self, dataframe: pd.DataFrame) -> str:
        """
        Explain query results in business language.
        """

        prompt = f"""
You are a Senior Data Analyst.

Explain these query results in simple business language.

Data:

{dataframe.to_markdown(index=False)}
"""

        return self.ai.ask(prompt)