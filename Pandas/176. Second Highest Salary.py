import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """Return the second highest salary of an employee.
    If there is no second highest salary, return null dataframe."""

    # Drop duplicates
    df = employee.drop_duplicates(subset=["salary"])["salary"]

    # Check if there is a second highest salary
    if len(df) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})

    # Return the second highest salary
    second_highest_salary = df.nlargest(2).iloc[-1]

    return pd.DataFrame({"SecondHighestSalary": [second_highest_salary]})
