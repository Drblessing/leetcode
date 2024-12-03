import pandas as pd
from typing import List


def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    """The problem asks us to create a DataFrame from a given 2D list containing student IDs and ages. We need to ensure that the DataFrame has two columns named 'student_id' and 'age' and is in the same order as the original 2D list."""

    # Dictionary method
    # Zip the column names and the 2D list
    data = dict(zip(["student_id", "age"], zip(*student_data)))
    print(data)

    # Create a DataFrame from the 2D list
    return pd.DataFrame(student_data, columns=["student_id", "age"])


# Example
student_data = [[1, 15], [2, 11], [3, 11], [4, 20]]
df = createDataframe(student_data)
