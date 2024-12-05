import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    """Find actors and directors who cooperated at least three times."""

    # Group by actor and director and count the occurrences.
    df = actor_director.groupby(["actor_id", "director_id"]).count()

    # Get the rows with a count of at least 3.
    df = df[df["timestamp"] >= 3]

    # Reset the index and drop the timestamp column.
    df = df.reset_index().drop("timestamp", axis=1)

    return df
