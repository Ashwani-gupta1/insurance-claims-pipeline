from src.ingestion.reader import DataReader


def test_csv_ingestion():

    reader = DataReader()

    df = reader.read(
        "data/sample/claims.csv"
    )

    assert len(df) == 5

    assert "claim_id" in df.columns

    assert "claim_amount" in df.columns