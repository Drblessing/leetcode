import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sal = employee.salary.drop_duplicates().sort_values(ascending=False)
    if len(sal) < N or N < 1:
        x = None
    else:
        x = sal.iloc[N - 1]
    return pd.DataFrame({f"getNthHighestSalary({N})": [x]})
