import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """Rename the columns:
    'id' to 'student_id',
    'first' to 'first_name',
    'last' to 'last_name',
    'age' to 'age_in_years'."""
    return students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
