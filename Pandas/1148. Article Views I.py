import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    """Return the authors who viewed at least one of their own articles.
    Return the result in ascending order with column name as 'id'."""

    views = views[views["author_id"] == views["viewer_id"]][["author_id"]]

    views = (
        views.rename(columns={"author_id": "id"}).drop_duplicates().sort_values("id")
    )

    return views
