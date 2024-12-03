import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    """Find the employee with the highest salary in each department."""

    # Check if the dataframes are empty
    if employee.empty or department.empty:
        return pd.DataFrame(columns=["Department", "Employee", "Salary"])

    # Rename the columns to avoid ambiguity, id -> departmentId
    department = department.rename(columns={"id": "departmentId", "name": "Department"})

    # name -> Employee, salary -> Salary
    employee = employee.rename(columns={"name": "Employee", "salary": "Salary"})

    # Merge the two dataframes on departmentId
    df = employee.merge(department, on="departmentId")

    # Group by Department
    df = df.groupby("departmentId")

    # Select the employee with the highest salary in each department,
    # including ties
    df = df.apply(lambda x: x[x["Salary"] == x["Salary"].max()])

    # Reset the index
    df = df.reset_index(drop=True)

    return df[["Department", "Employee", "Salary"]]
