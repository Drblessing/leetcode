import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    """Calculate the total time spent by each employee, each day."""

    employees["time"] = employees["out_time"] - employees["in_time"]

    time = employees.groupby(["emp_id", "event_day"])["time"].sum().reset_index()

    dict_rename = {"time": "total_time", "event_day": "day"}

    return time.rename(columns=dict_rename)
