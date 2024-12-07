import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """Get the fraction of players who played on the day after their first day."""

    # Get the number of players
    n = activity["player_id"].nunique()

    # Get the first day each player played
    first_days = activity.groupby("player_id")["event_date"].min().reset_index()
    first_days.rename(columns={"event_date": "first_day"}, inplace=True)

    # Merge to find if the player played on the next day
    first_days["next_day"] = first_days["first_day"] + pd.Timedelta(days=1)

    # Check if players played on the day after their first day
    returned = pd.merge(
        first_days,
        activity,
        left_on=["player_id", "next_day"],
        right_on=["player_id", "event_date"],
        how="inner",
    )

    # Calculate the fraction
    fraction = len(returned) / n

    # Round the fraction to two decimal places
    fraction = round(fraction, 2)

    # Create a DataFrame with the fraction
    result = pd.DataFrame({"fraction": [fraction]})

    return result
