import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Get unique salaries, sort in descending order, and fetch the second highest (if exists)
    second_highest = (
        employee["salary"].drop_duplicates().nlargest(2).iloc[-1]
        if len(employee["salary"].drop_duplicates()) > 1
        else None
    )

    # Return as a DataFrame
    return pd.DataFrame({"SecondHighestSalary": [second_highest]})
