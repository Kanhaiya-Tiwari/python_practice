PHASE 2: LOOPS AND CONTROL FLOW - INTERVIEW QUESTIONS & ANSWERS

=== IF-ELSE STATEMENTS ===

1. What are conditional statements?
Statements that allow you to execute different code based on conditions.
Example: if age >= 18: print("Adult")

2. What are the types of conditional statements?
if - Executes code if condition is true
elif (else if) - Executes if previous conditions are false
else - Executes if all previous conditions are false

3. What is the difference between if and elif?
if starts a new condition check
elif is checked only if the previous if was false
elif allows multiple conditions to be checked in sequence

4. What is the difference between elif and else?
elif checks a specific condition: elif age < 13: (has a condition)
else doesn't check condition: else: (no condition, always true if reached)

5. What are comparison operators used in if statements?
== Equal to
!= Not equal to
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to

6. What are logical operators?
and - Both conditions must be true
or - At least one condition must be true
not - Negates the condition

Example: if age >= 18 and has_license:

7. What is a ternary operator?
A short way to write if-else in one line.
Syntax: value_if_true if condition else value_if_false
Example: status = "Adult" if age >= 18 else "Child"

8. What is nested if statement?
An if statement inside another if statement.
Used when you need multiple levels of conditions.

9. What is a switch-case statement in Python? (Prior to Python 3.10)
Python didn't have switch-case. Use if-elif-else instead.
From Python 3.10+, use match-case statement.

10. How do you write multiple conditions in one line?
Using logical operators (and, or, not)
Example: if x > 0 and x < 10:

=== FOR LOOPS ===

11. What is a for loop?
A loop that repeats a block of code a specific number of times.
Example: for i in range(5): print(i)

12. What is the difference between for and while loop?
for loop runs for a specific number of iterations (known beforehand)
while loop runs while a condition is true (unknown iterations count)

13. How do you use range() in a for loop?
range(5) gives 0, 1, 2, 3, 4
range(1, 5) gives 1, 2, 3, 4
range(1, 10, 2) gives 1, 3, 5, 7, 9 (step of 2)

Example: for i in range(5): print(i)

14. What is enumerate()?
enumerate() gives both index and value while looping through a list.
Example:
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

15. What is zip()?
zip() combines two or more iterables.
Example:
for a, b in zip([1, 2], ['x', 'y']):
    print(a, b)  # (1, x) then (2, y)

16. How do you loop through a string?
for char in "Hello": print(char)
Output: H e l l o

17. How do you loop through a list?
for item in [1, 2, 3]: print(item)

18. How do you loop through a dictionary?
for key in dict: print(key)  # Loops through keys
for value in dict.values(): print(value)  # Loops through values
for key, value in dict.items(): print(key, value)  # Loops through both

19. What is list comprehension?
A short way to create a new list by applying an operation to each item.
Example: squares = [x**2 for x in range(5)]
Result: [0, 1, 4, 9, 16]

20. What is the difference between for and while loop in terms of use?
Use for when you know how many iterations (counting)
Use while when you don't know iterations (conditional loops)

=== WHILE LOOPS ===

21. What is a while loop?
A loop that repeats code while a condition is true.
Example: while x < 5: x += 1

22. When should you use while loop?
Use when the number of iterations is unknown
Use for asking user input until valid
Use for event-driven loops

23. What is an infinite loop?
A loop that never ends because the condition is always true.
Example: while True: print("Infinite loop!")
To exit: use break or Ctrl+C

24. What problems can infinite loops cause?
Program hangs and becomes unresponsive
Consumes CPU resources
Can crash the system if memory is exhausted

25. How do you exit an infinite loop?
Press Ctrl+C in the terminal
Use break statement in the code
Close the program window

=== LOOP CONTROL ===

26. What is break statement?
Exits the loop immediately.
Example:
for i in range(10):
    if i == 5:
        break  # Loop stops
    print(i)

27. What is continue statement?
Skips the current iteration and goes to the next one.
Example:
for i in range(5):
    if i == 2:
        continue  # Skips 2
    print(i)  # Output: 0 1 3 4

28. What is pass statement?
A null statement; does nothing. Used as a placeholder.
Example:
for i in range(5):
    pass  # Does nothing

29. What is the difference between break and continue?
break exits the loop completely
continue skips current iteration and continues with next

30. What is else clause in loops?
Executes when loop completes normally (without break).
Example:
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed")  # This will print

=== NESTED LOOPS ===

31. What are nested loops?
A loop inside another loop.
Example:
for i in range(3):
    for j in range(2):
        print(i, j)

32. How do you break out of nested loop?
break only exits the innermost loop
To exit outer loop, use flag or function return

33. What is the time complexity of nested loops?
If outer loop runs n times and inner loop runs m times: O(n*m)
Example: 3x3 loop = 9 iterations

34. What are practical uses of nested loops?
Creating 2D patterns (matrices, tables)
Comparing elements in lists
Matrix operations

35. How do you print a pyramid using nested loops?
Example:
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

=== PRACTICE QUESTIONS ===

36. Write a program to print numbers 1 to 10.
for i in range(1, 11):
    print(i)

37. Write a program to find sum of first 100 numbers.
total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050

38. Write a program to check if a number is prime.
num = 17
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")

39. Write a program to print multiplication table.
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

40. Write a program to reverse a number.
num = 12345
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(reversed_num)  # 54321
