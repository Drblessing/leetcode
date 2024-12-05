import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    """Find all classes with at least 5 students."""

    courses = courses.value_counts("class").to_frame().reset_index()

    return courses[courses["count"] >= 5][["class"]]
