import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    """Find the biggest single number."""

    # Get the value counts of the numbers.
    value_counts = my_numbers["number"].value_counts()

    # Filter for the numbers that only appear once.
    single_numbers = value_counts[value_counts == 1].index

    # If there are no single numbers, return an empty DataFrame.
    if single_numbers.empty:
        return pd.DataFrame()

    # Find the biggest single number.
    biggest_single_number = single_numbers.max()

    # Return the biggest single number.
    return pd.DataFrame({"number": [biggest_single_number]})
