import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    """Write a solution to calculate the bonus of each employee.
    The bonus of an employee is 100% of their salary if the ID of the employee is an odd number
    and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
    """

    employees["bonus"] = employees.apply(
        lambda x: (
            x["salary"] if x["employee_id"] % 2 != 0 and x["name"][0] != "M" else 0
        ),
        axis=1,
    )
    return employees[["employee_id", "bonus"]].sort_values("employee_id")
