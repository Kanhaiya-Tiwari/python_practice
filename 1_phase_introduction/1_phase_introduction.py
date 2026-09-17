# Practice Tasks

# Print your name, age, and profession using an f-string.
name = "Kanha"
age = 22
profession = "DevOps Engineer"
print(f"My name is {name}, I am {age} years old, and I work as a {profession}.")

# Take two numbers as input and print their sum, difference, product, and quotient.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")

# Swap two variables without using a third variable.
a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")

# Convert "100" (string) to an integer and add 50.
number = int("100")
result = number + 50
print(f"Result: {result}")

# Convert [1, 2, 2, 3, 4, 4] into a set and print the result.
list_with_duplicates = [1, 2, 2, 3, 4, 4]
unique_set = set(list_with_duplicates)
print(f"Unique elements: {unique_set}")

# Ask the user for their age and print whether they are eligible to vote using an if statement.
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Check whether "python" is present in the string "I love python programming" using the in operator.
text = "I love python programming"
if "python" in text:
    print("The word 'python' is present in the string.")
else:
    print("The word 'python' is not present in the string.")