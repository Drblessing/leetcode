import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    """
        Table: Accounts

    +-------------+------+
    | Column Name | Type |
    +-------------+------+
    | account_id  | int  |
    | income      | int  |
    +-------------+------+
    account_id is the primary key (column with unique values) for this table.
    Each row contains information about the monthly income for one bank account.



    Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

        "Low Salary": All the salaries strictly less than $20000.
        "Average Salary": All the salaries in the inclusive range [$20000, $50000].
        "High Salary": All the salaries strictly greater than $50000.

    The result table must contain all three categories. If there are no accounts in a category, return 0.

    Return the result table in any order.

    The result format is in the following example.

    """

    # Solve without SQL

    # Create a new column to categorize the salary
    def categorize_salary(income):
        if income < 20000:
            return "Low Salary"
        elif 20000 <= income <= 50000:
            return "Average Salary"
        else:
            return "High Salary"

    accounts["salary_category"] = accounts["income"].apply(categorize_salary)

    salaries = ["Low Salary", "Average Salary", "High Salary"]

    # Count the number of accounts in each category
    rename_columns = {"salary_category": "category", 0: "accounts_count"}
    accounts = (
        accounts.groupby("salary_category")
        .size()
        .reset_index()
        .rename(columns=rename_columns)
    )

    # Check for missing categories and add them with 0 accounts
    for salary in salaries:
        if salary not in accounts["category"].unique():
            # Use concat to add the missing category
            accounts = pd.concat(
                [
                    accounts,
                    pd.DataFrame([[salary, 0]], columns=["category", "accounts_count"]),
                ]
            )

    return accounts
