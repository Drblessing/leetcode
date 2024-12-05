import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    """Group sold products by the date."""

    # Define a function to aggregate products.
    def aggregate_products(x):
        return ",".join(sorted(set(x)))

    # Group by the sell_date column.
    df = (
        activities.groupby("sell_date")["product"]
        .agg(["nunique", aggregate_products])
        .reset_index()
    )

    rename_dict = {"nunique": "num_sold", "aggregate_products": "products"}
    # Return the result table ordered by sell_date.
    df = df.rename(columns=rename_dict).sort_values("sell_date")

    return df
