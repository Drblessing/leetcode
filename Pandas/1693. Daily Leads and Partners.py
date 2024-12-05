import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    """For each date_id and make_name,
    find the number of distinct lead_id's and distinct partner_id's."""

    # Group by date_id and make_name.
    df = daily_sales.groupby(["date_id", "make_name"])[
        ["lead_id", "partner_id"]
    ].nunique()

    # Reset the index.
    df = df.reset_index()

    # Rename the columns.
    df = df.rename(columns={"lead_id": "unique_leads", "partner_id": "unique_partners"})

    return df
