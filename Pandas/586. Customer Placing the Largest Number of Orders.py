import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """Find the customer who placed the largest number of orders."""

    # Check if the DataFrame is empty
    if orders.empty:
        return pd.DataFrame({"customer_number": []})

    customer_number = orders["customer_number"].value_counts().idxmax()

    return pd.DataFrame({"customer_number": [customer_number]})
