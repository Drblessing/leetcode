import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """Reshape the data in the report DataFrame using the melt function.
        Input:
    +-------------+-----------+-----------+-----------+-----------+
    | product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
    +-------------+-----------+-----------+-----------+-----------+
    | Umbrella    | 417       | 224       | 379       | 611       |
    | SleepingBag | 800       | 936       | 93        | 875       |
    +-------------+-----------+-----------+-----------+-----------+
    Output:
    +-------------+-----------+-------+
    | product     | quarter   | sales |
    +-------------+-----------+-------+
    | Umbrella    | quarter_1 | 417   |
    | SleepingBag | quarter_1 | 800   |
    | Umbrella    | quarter_2 | 224   |
    | SleepingBag | quarter_2 | 936   |
    | Umbrella    | quarter_3 | 379   |
    | SleepingBag | quarter_3 | 93    |
    | Umbrella    | quarter_4 | 611   |
    | SleepingBag | quarter_4 | 875   |
    +-------------+-----------+-------+
    """

    return report.melt(
        id_vars="product",
        var_name="quarter",
        value_name="sales",
        value_vars=["quarter_1", "quarter_2", "quarter_3", "quarter_4"],
    )
