import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """Create a new column 'bonus' in the given DataFrame, which is
    double the value of the 'salary' column."""
    employees["bonus"] = employees["salary"] * 2
    return employees
