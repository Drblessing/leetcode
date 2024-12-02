import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """Pivot the dataframe to make the records represent temperatures for a
    specific month, and each city is a columns.

    Pivoting a table means to rotate the table around a column. It usually transforms
    a long table into a wide table."""

    return weather.pivot_table(index="Date", columns="City", values="Temperature")
