import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """Find customers who never ordered anything."""

    # First solution, use isin
    # Target columns:
    # customers: id
    # orders: customerId

    def is_not_in(df1, col1, df2, col2):
        return ~df1[col1].isin(df2[col2])

    result = customers[is_not_in(customers, "id", orders, "customerId")]

    # Rename name as Customers
    return result[["name"]].rename(columns={"name": "Customers"})

    """
    # Second solution, use merge
    # Target columns:
    # customers: id
    # orders: customerId
    merged = pd.merge(
        customers,
        orders,
        left_on="id",
        right_on="customerId",
        how="left",
        suffixes=("_customer", "_order"),
    )

    # Select records where customerId is NaN
    result = merged[merged["customerId"].isna()]

    # Rename name as Customers
    return result[["name"]].rename(columns={"name": "Customers"})
    """
