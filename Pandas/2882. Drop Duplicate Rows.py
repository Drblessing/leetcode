import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows based on the 'email' column."""
    return customers.drop_duplicates(subset="email")
