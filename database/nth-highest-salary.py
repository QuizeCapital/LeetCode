import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Remove duplicates and sort in descending order (highest first)
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if N is within valid range
    if N < 1 or N > len(unique_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Get the Nth highest salary (N-1 because of zero-based indexing)
    nth_highest = unique_salaries.iloc[N-1]
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})