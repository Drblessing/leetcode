import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    """Find users with valid emails. Valid emails start with letters and contain
    normal characters, and the domain is @leetcode.com."""
