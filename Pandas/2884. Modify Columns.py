import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """Double the values in the 'salary' column."""
    employees["salary"] = employees["salary"] * 2
    return employees
