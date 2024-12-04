import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    """Return the scores ordered by rank."""

    # Calculate the rank of each score
    scores["rank"] = scores["score"].rank(method="dense", ascending=False).astype(int)

    # Sort the scores by rank and drop the rank
    scores = scores.sort_values("rank").drop(columns="id")

    return scores
