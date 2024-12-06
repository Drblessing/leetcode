import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    """Find the managers with at least five direct reports"""

    # Group by managerId
    df = employee.groupby("managerId", as_index=False).size()

    # Get managers with at least 5 direct reports
    df = df[df["size"] >= 5][["managerId"]]

    # Rename managerId to id
    df = df.rename(columns={"managerId": "id"})

    # Join back with employee to get the manager's name
    df = pd.merge(df, employee, how="left", on="id")

    return df.rename(columns={"managerId": "name"})
