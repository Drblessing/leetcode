import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing data only in the 'name' column."""
    return students.dropna(subset=["name"])
