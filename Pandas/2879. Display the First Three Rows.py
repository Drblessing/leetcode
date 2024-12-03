import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """Select the first three rows of the given DataFrame."""
    return employees.head(3)

    # Alternatively, we can use the iloc method to achieve the same result:
    # return employees.iloc[:3]
