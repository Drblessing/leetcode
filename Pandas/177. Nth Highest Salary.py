import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """Return the nth_highest salary from the employee table, not counting duplicates.
    If the nth highest salary does not exist, return a null dataframe."""
