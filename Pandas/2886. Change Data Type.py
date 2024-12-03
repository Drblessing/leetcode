import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    """Change the data type of the 'grade' column from float to integers."""
    students["grade"] = students["grade"].astype(int)
    return students

    # assign
    # return students.assign(grade=students["grade"].astype(int))
