
# Write a function that adds two numbers and returns the result.
def calc_sum(a,b):
    return a + b
 
sum = calc_sum( 3,3)
print(sum)

# Create a function with a default argument (country="India").
def greet(name, country="India"):
    print(f"Hello {name} from {country}")
greet("kanha")
# Use keyword arguments to create an employee record.
def create_employee(name, age, salary):
    return {"name": name, "age": age, "salary": salary}
employee = create_employee(name="kanha", age=30, salary=50000)
print(employee)

# Write a function using *args to calculate the sum of any number of integers.
def calculate_sum(*args):
    return sum(args)
result = calculate_sum(1, 2, 3, 4, 5)
print(result)
# Write a function using **kwargs to print employee details.
def print_employee_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_employee_details(name="kanha", age=30, salary=50000)
# Write a recursive function to calculate the factorial of a number.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))