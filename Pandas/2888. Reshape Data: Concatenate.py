import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """Concatenate two DataFrames."""
    return pd.concat([df1, df2])
