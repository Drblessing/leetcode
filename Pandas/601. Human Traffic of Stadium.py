import pandas as pd


def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    """Return rows with consecutive human traffic over 100 for
    three days in a row."""

    # Create a mask for the condition.
    mask = (
        (stadium["human_traffic"] > 100)
        & (stadium["human_traffic"].shift(1) > 100)
        & (stadium["human_traffic"].shift(2) > 100)
    )

    return stadium[mask]
