import pandas as pd


def sales_person(
    sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame
) -> pd.DataFrame:
    """Return the sales people without orders related to the "RED" company."""

    # Merge companies with orders.
    df = pd.merge(orders, company, how="inner")

    # Only keep RED company.
    df = df[(df["name"] == "RED")][["sales_id"]]

    # Sales people without orders related to the RED company.
    company = sales_person[~sales_person["sales_id"].isin(df["sales_id"])]

    return company[["name"]]
