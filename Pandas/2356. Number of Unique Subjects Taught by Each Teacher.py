import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    """Calculate the number of unique subjects taught by each teacher."""

    # Group by teacher and count unique subjects
    return (
        teacher.groupby("teacher_id")["subject_id"]
        .nunique()
        .reset_index()
        .rename(columns={"subject_id": "cnt"})
    )
