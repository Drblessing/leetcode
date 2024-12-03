import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    """Fix capitalized names in a DataFrame."""
    users["name"] = users["name"].str.capitalize()
    return users.sort_values("user_id")
