import pandas as pd


def average_selling_price(
    prices: pd.DataFrame, units_sold: pd.DataFrame
) -> pd.DataFrame:
    # 1. Combine prices with units_sold data, matching rows by product_id.
    #    Use a left merge to keep all price records, even if no units were sold.
    merged = pd.merge(prices, units_sold, on="product_id", how="left")

    # 2. After merging, filter rows so that the purchase_date of a sale
    #    falls within the start_date and end_date range for that product's price.
    valid_date_mask = (merged["purchase_date"] >= merged["start_date"]) & (
        merged["purchase_date"] <= merged["end_date"]
    )
    merged = merged[valid_date_mask]

    # 3. Group by product_id to:
    #    - sum up total_units (units sold for that product)
    #    - sum up total_revenue (units * price)
    #    We calculate total_revenue using a lambda that multiplies units
    #    by their corresponding price.
    grouped = merged.groupby("product_id", as_index=False).agg(
        total_revenue=("units", lambda x: (x * merged.loc[x.index, "price"]).sum()),
        total_units=("units", "sum"),
    )

    # 4. Ensure every product from the Prices table is included in the result.
    #    If a product sold no units, it won't appear in 'grouped',
    #    so we merge back with a DataFrame of all unique product_ids.
    all_products = pd.DataFrame({"product_id": prices["product_id"].unique()})
    result = pd.merge(all_products, grouped, on="product_id", how="left")

    # Fill in missing revenue/units with 0 for products that had no sales.
    result = result.fillna({"total_units": 0, "total_revenue": 0})

    # 5. Calculate the average price:
    #    If no units were sold, average_price = 0.
    #    Otherwise, average_price = total_revenue / total_units (rounded to 2 decimals).
    def compute_average_price(row):
        if row["total_units"] == 0:
            return 0
        else:
            return round(row["total_revenue"] / row["total_units"], 2)

    result["average_price"] = result.apply(compute_average_price, axis=1)

    # 6. Return only the product_id and average_price columns, sorted by product_id.
    final_result = (
        result[["product_id", "average_price"]]
        .sort_values("product_id")
        .reset_index(drop=True)
    )

    return final_result
