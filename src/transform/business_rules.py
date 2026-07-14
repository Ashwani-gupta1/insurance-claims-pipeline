from src.utils.logger import get_logger


logger = get_logger(__name__)


def classify_claim_amount(amount):
    """
    Categorize claims based on amount.
    """

    if amount < 2000:
        return "Small Claim"

    elif amount < 5000:
        return "Medium Claim"

    else:
        return "Large Claim"



def assign_priority(status, amount):
    """
    Assign business priority.
    """

    if status == "Open" and amount >= 5000:
        return "High"

    elif status == "Open":
        return "Normal"

    else:
        return "Low"