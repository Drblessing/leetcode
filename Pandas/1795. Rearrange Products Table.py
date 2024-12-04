import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    """Rearrange the products table.
    Melt the columns into rows.
    """

    # Melt the columns into rows
    products = products.melt(id_vars="product_id", var_name="store", value_name="price")

    # Remove null values
    products = products.dropna()

    return products
