import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    df = world[(world["area"] >= 3_000_000) | (world["population"] >= 25_000_000)]

    return df[["name", "population", "area"]]
