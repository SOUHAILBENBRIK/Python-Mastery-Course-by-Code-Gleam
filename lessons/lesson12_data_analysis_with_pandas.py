"""
Lesson 12: Data Analysis with Pandas
Objective: Understand how to manipulate and analyze data using the Pandas library.
"""

import pandas as pd

# Creating a DataFrame with Tunisian data
data = {
    "Name": ["Ahmed", "Sara", "Youssef", "Leila", "Khaled"],
    "Age": [24, 30, 22, 35, 28],
    "City": ["Tunis", "Sfax", "Sousse", "Gabès", "Kairouan"],
    "Salary": [1500, 1800, 1200, 2000, 1600]  # Salaries in Tunisian Dinar (TND)
}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)

# Analyzing data
print("\nStatistical Summary:")
print(df.describe())  # Output: Statistical summary of the numeric columns.

# Filtering data for young people
young_people = df[df["Age"] < 25]
print("\nYoung People (Age < 25):")
print(young_people)  # Output: Rows where Age is less than 25.

# Selecting a specific column
print("\nNames of All Employees:")
print(df["Name"])  # Output: List of all names.

# Adding a new column for years of experience
df["Experience"] = [2, 5, 1, 7, 3]  # Years of experience
print("\nDataFrame After Adding Experience Column:")
print(df)

# Modifying an existing column (Salary increase)
df["Salary"] = df["Salary"] * 1.1  # Giving a 10% raise
print("\nDataFrame After Salary Raise:")
print(df)

# Dropping a column (City)
df = df.drop(columns=["City"])  # Remove the 'City' column
print("\nDataFrame After Dropping 'City' Column:")
print(df)

# Grouping data by age and calculating average salary
average_salary_by_age = df.groupby("Age")["Salary"].mean()  # Average salary by age
print("\nAverage Salary by Age:")
print(average_salary_by_age)

# Sorting the DataFrame by Salary
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nDataFrame Sorted by Salary (Descending):")
print(sorted_df)

# EXERCISES:
# 1. Create a DataFrame from a CSV file and display the first five rows.
# (Assuming you have a CSV file named 'employees.csv')
# df_from_csv = pd.read_csv('employees.csv')
# print(df_from_csv.head())

# 2. Write a program to calculate the average age from the DataFrame.
average_age = df["Age"].mean()
print("\nAverage Age of Employees:")
print(average_age)

# 3. Find the employee with the highest salary.
highest_salary = df[df["Salary"] == df["Salary"].max()]
print("\nEmployee with the Highest Salary:")
print(highest_salary)

# 4. Count the number of employees in each age group (e.g., 20s, 30s).
age_groups = pd.cut(df["Age"], bins=[20, 30, 40], labels=["20s", "30s"])
age_group_counts = df.groupby(age_groups).size()
print("\nNumber of Employees in Each Age Group:")
print(age_group_counts)
