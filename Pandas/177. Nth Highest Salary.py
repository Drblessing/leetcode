import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """Return the Nth highest salary of an employee.
    If there is no Nth highest salary, return null dataframe."""

    # Create column name
    column_name = f"getNthHighestSalary({N})"

    # Drop duplicates
    df = employee.drop_duplicates(subset=["salary"])["salary"]

    # Check if there is a Nth highest salary
    if len(df) < N or N < 1:
        return pd.DataFrame({column_name: [None]})

    # Return the Nth highest salary
    nth_highest_salary = df.nlargest(N).iloc[-1]

    return pd.DataFrame({column_name: [nth_highest_salary]})
