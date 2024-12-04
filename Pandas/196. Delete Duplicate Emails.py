import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """Delete duplicate emails from a dataframe, in place."""

    # Sort the dataframe by id
    person.sort_values(by="id", inplace=True)

    # Drop duplicates
    person.drop_duplicates(subset=["email"], inplace=True)
