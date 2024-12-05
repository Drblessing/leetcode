import pandas as pd


def replace_employee_id(
    employees: pd.DataFrame, employee_uni: pd.DataFrame
) -> pd.DataFrame:
    """Join the tables and return employees with unique identifier. If they don't
    have a identifier, return None.
    """

    # Merge the tables.
    df = pd.merge(employees, employee_uni, on="id", how="left")

    # Drop id col.
    df = df.drop(columns=["id"])

    return df
