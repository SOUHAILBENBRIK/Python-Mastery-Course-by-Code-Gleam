# Problem: Data Class Example
# Question: Use dataclasses to define a class for storing and displaying employee information.








from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    id: int
    department: str

# Example usage
emp = Employee("John Doe", 101, "Engineering")
print(emp)  # Output: Employee(name='John Doe', id=101, department='Engineering')
