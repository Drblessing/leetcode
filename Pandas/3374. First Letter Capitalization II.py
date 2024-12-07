import pandas as pd


def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    """Capitalize content in a df."""

    # Use the title() method.
    user_content["converted_text"] = user_content["content_text"].apply(
        lambda x: x.title()
    )

    return user_content.rename(columns={"content_text": "original_text"})
