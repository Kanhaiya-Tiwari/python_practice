# Practice Exercises
# Print numbers from 1 to 20 using a for loop.
for i in range(1, 21):
    print(i)
# Print only the even numbers between 1 and 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
# Take a number from the user and print its multiplication table (1–10).
numbers = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{numbers} x {i} = {numbers * i}")
# Print every character of your name using a loop.
name = "Kanha"
for char in name:
    print(char)
# Use enumerate() to print the index and value of a list of five programming languages.
languages = ["Python", "Java", "C++", "C#", "JavaScript"]
for index, language in enumerate(languages):
    print(f"Index: {index}, Language: {language}")
# Use zip() to print employee names with their salaries from two separate lists.
employee_names = ["Alice", "Bob", "Charlie"]
employee_salaries = [50000, 60000, 70000]
for name, salary in zip(employee_names, employee_salaries):
    print(f"Name: {name}, Salary: {salary}")
# Print numbers from 1 to 100, but stop when you reach 50 using break.
for i in range(1, 101):
    if i == 51:
        break
    print(i)
# Print numbers from 1 to 20, skipping multiples of 3 using continue.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)            
# Use a while loop to count down from 10 to 1.
count = 10
while count > 0:
    print(count)
    count -= 1      
# Build a simple login program that allows 3 password attempts using a while loop.
password = "secret"
attempts = 0
while attempts < 3:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Login successful!")
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1
else:
    print("Too many failed attempts. Access denied.")


    # print number from 1 to 100

    count = 1
    while count <= 100:
        print(count)
        count += 13

# found the specific numbers in the list

numbers = [ 1, 33, 323, 3, 44, 97, 48, 84]

x = 44
i = 0
while i < len(numbers):
    if (numbers[i] == x ):
        print ("numbers found in index :" , i )
    i += 1    
