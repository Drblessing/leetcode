import pandas as pd


def students_and_examinations(
    students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame
) -> pd.DataFrame:
    """Return the number of times each student attended each exam."""

    # Cross join each student on each subject.
    students_subjects = pd.merge(students, subjects, how="cross")

    # Calculate the number of times each student attended each exam from examinations.
    examinations = (
        examinations.groupby(["student_id", "subject_name"]).size().reset_index()
    )

    # Rename the columns.
    examinations = examinations.rename(columns={0: "attended_exams"})

    # Merge the tables.
    df = pd.merge(
        students_subjects, examinations, how="left", on=["student_id", "subject_name"]
    )

    # Fill NaN values with 0.
    df["attended_exams"] = df["attended_exams"].fillna(0)

    # Sort by student_id and subject_name.
    df = df.sort_values(by=["student_id", "subject_name"])

    return df
