# Imagine the client gives us these files:

# claims.csv
# customers.xlsx
# notes.json
# providers.parquet

# Instead of hardcoding:
# pd.read_csv(...)

# our application should automatically detect the file type and decide how to read it.
# This is called extensibility. Later, if the client adds XML or Parquet files, we only need to update this module.

from pathlib import Path


def get_file_extension(file_path: str) -> str:
    """
    Returns the file extension in lowercase.

    Example:
        claims.csv  -> .csv
        data.XLSX   -> .xlsx
    """
    return Path(file_path).suffix.lower()