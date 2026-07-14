from ollama import chat
from src.utils.logger import get_logger


logger = get_logger(__name__)


class AIClient:
    """
    Handles communication with the local Ollama LLM.
    """

    def __init__(self, model: str = "llama3.2"):
        self.model = model

    def ask(self, prompt: str) -> str:
        """
        Sends a prompt to the LLM and returns the response.
        """

        logger.info("Sending prompt to AI")

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        logger.info("Received response from AI")

        return response.message.content.strip()