import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    """Find users with valid emails. Valid emails start with letters and contain
    normal characters, and the domain is @leetcode.com.
    Normal charactesr are letters, digits, and the characters . and _."""

    # Extract the emails
    emails = users["mail"]

    # Check if the email is valid
    valid = emails.str.match(r"^[a-zA-Z][a-zA-Z0-9._-]*@leetcode[.]com$")

    return users[valid]
