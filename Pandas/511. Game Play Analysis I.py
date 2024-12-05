import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """Find the first login date of each player."""

    # Use the min function to find the first login date of each player.
    # Group by the player_id column.
    activity = activity.groupby("player_id")

    # Use the min function on the event_date column.
    activity = activity["event_date"].min()

    # Reset the index.
    activity = activity.reset_index()

    # Rename the column to first_login.
    activity = activity.rename(columns={"event_date": "first_login"})

    return activity
