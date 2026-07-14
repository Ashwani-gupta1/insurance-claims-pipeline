import pandas as pd

from src.transform.claim_transformer import ClaimTransformer


def test_claim_transformation():

    df = pd.DataFrame(
        {
            "claim_amount": [7000],
            "status": ["Open"]
        }
    )


    transformer = ClaimTransformer()

    result = transformer.transform(df)


    assert result.iloc[0]["claim_category"] == "Large Claim"

    assert result.iloc[0]["priority"] == "High"