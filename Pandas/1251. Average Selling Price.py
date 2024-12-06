import pandas as pd


def average_selling_price(
    prices: pd.DataFrame, units_sold: pd.DataFrame
) -> pd.DataFrame:
    """Calculate the average selling price of units sold."""

    # Merge the tables based on product_id.
    merged = pd.merge(prices, units_sold, on="product_id", how="left")

    # Filter to ensure the purchase_date falls within price intervals.
    mask = (merged["purchase_date"] >= merged["start_date"]) & (
        merged["purchase_date"] <= merged["end_date"]
    )
    merged = merged[mask]

    # Calculate the total revenue for each purchase.
    merged["total_revenue"] = merged["price"] * merged["units"]

    # Group the data for each product into units and revenue.
    df = merged.groupby("product_id").agg(
        total_revenue=("total_revenue", "sum"), units_sold=("units", "sum")
    )

    # Calculate the average price.
    df["average_price"] = df["total_revenue"] / df["units_sold"]
    df = df.reset_index()[["product_id", "average_price"]]

    # Round the average price to two decimal places.
    df["average_price"] = df["average_price"].round(2)

    # Get set of product_ids from prices table.
    product_ids = prices["product_id"].unique()

    # Get the missing product_ids from the units_sold table.
    missing_product_ids = set(df["product_id"]) ^ set(product_ids)

    # Create a DataFrame for the missing product_ids.
    missing_df = pd.DataFrame(
        {
            "product_id": list(missing_product_ids),
            "average_price": [0] * len(missing_product_ids),
        }
    )

    # Concatenate the missing product_ids to the DataFrame.
    df = pd.concat([df, missing_df])

    return df
