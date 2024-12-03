import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """List the names of the animals that weigh more than 100 kilograms.
    Return the animals sorted by weight in descending order."""

    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[
        ["name"]
    ]
