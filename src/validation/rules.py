from datetime import datetime


def validate_required_fields(row):
    """
    Check mandatory claim fields.
    """

    required_fields = [
        "claim_id",
        "claim_amount",
        "claim_date"
    ]

    errors = []

    for field in required_fields:
        if row.get(field) is None or row.get(field) == "":
            errors.append(
                f"Missing required field: {field}"
            )

    return errors


def validate_claim_amount(row):
    """
    Claim amount must be positive.
    """

    errors = []

    amount = row.get("claim_amount")

    if amount is not None:
        if amount <= 0:
            errors.append(
                "Claim amount must be greater than zero"
            )

    return errors


def validate_claim_date(row):
    """
    Claim date cannot be in the future.
    """

    errors = []

    claim_date = row.get("claim_date")

    if claim_date:

        if isinstance(claim_date, str):
            claim_date = datetime.strptime(
                claim_date,
                "%Y-%m-%d"
            )

        today = datetime.today()

        if claim_date.date() > today.date():
            errors.append(
                "Claim date cannot be in the future"
            )

    return errors