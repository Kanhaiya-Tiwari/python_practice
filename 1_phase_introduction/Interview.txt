PHASE 1: INTRODUCTION TO PYTHON - INTERVIEW QUESTIONS & ANSWERS

=== BASIC CONCEPTS ===

1. What is a variable?
A variable is a container that holds a value. It's like a named box where you can store data.
Example: name = "Alice"

2. What are data types?
Data types specify what type of value a variable can hold.
Main types: int (integers), float (decimals), str (strings), bool (True/False)

3. Difference between int and float?
int stores whole numbers without decimal points.
Example: age = 25
float stores numbers with decimal points.
Example: height = 5.8

4. What is type casting?
Converting one data type to another.
Example: x = int("50") converts string to integer

5. What is the difference between print() and input()?
print() displays output on the screen.
Example: print("Hello")
input() takes data from the user as input.
Example: name = input("Enter your name: ")

6. What are operators?
Operators perform operations on variables and values.
Types: Arithmetic (+, -, *, /), Comparison (==, !=, <, >), Logical (and, or, not)

7. What is the difference between = and ==?
= is assignment operator (assigns value to variable).
Example: x = 5
== is comparison operator (checks if values are equal).
Example: x == 5 returns True or False

8. What are comments?
Comments are lines that Python ignores. Used to explain code.
Single line: # This is a comment
Multiple line: """ This is a multi-line comment """

9. What is None?
None is a special value representing the absence of a value.
Example: x = None

10. What is the difference between strings, integers, and floats?
String: Text data enclosed in quotes. Example: "Hello"
Integer: Whole numbers without decimals. Example: 42
Float: Numbers with decimal points. Example: 3.14

=== OPERATORS ===

11. What are arithmetic operators?
+  Addition
-  Subtraction
*  Multiplication
/  Division
// Floor division (integer division)
%  Modulus (remainder)
** Exponentiation (power)

12. What is modulus operator (%)?
Returns the remainder after division.
Example: 10 % 3 = 1 (10 divided by 3 leaves remainder 1)

13. What is the difference between / and //?
/ performs regular division and returns float.
Example: 10 / 3 = 3.333...
// performs floor division and returns integer.
Example: 10 // 3 = 3

14. What are comparison operators?
== Equal to
!= Not equal to
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to

15. What are logical operators?
and - Returns True if both conditions are true
or - Returns True if either condition is true
not - Negates/reverses the condition

=== TYPE CASTING & CONVERSION ===

16. How do you convert a string to integer?
int("42") or int("42.5") converts to integer with error on non-numeric
Example: x = int("50")

17. How do you convert integer to string?
str(42) converts integer to string
Example: x = str(100)

18. What happens if you convert "abc" to integer?
It raises a ValueError because "abc" cannot be converted to integer
Example: int("abc") # Error!

19. How do you get the length of a string?
Using len() function
Example: len("Hello") returns 5

20. What is the difference between str() and repr()?
str() returns a string representation suitable for end users
repr() returns a string representation suitable for debugging

=== INPUT & OUTPUT ===

21. How do you take input from user?
Using input() function
Example: name = input("Enter your name: ")
Note: input() always returns a string

22. How do you display multiple values with print()?
print(a, b, c)
Example: print("Hello", "World")  # Hello World

23. How do you format output?
Using f-strings (modern): f"Value is {x}"
Using .format(): "Value is {}".format(x)
Using % operator: "Value is %d" % x

24. What is f-string?
F-string allows embedding variables directly in string.
Example: name = "Bob"; print(f"Hello {name}")

25. How do you print without newline?
Using end parameter in print()
Example: print("Hello", end="")

=== VARIABLES & NAMING ===

26. What are valid variable names?
Can contain letters, digits, underscores
Must start with letter or underscore
Case-sensitive
Example: my_var, _private, var123

27. What are invalid variable names?
Cannot start with a digit: 1var (invalid)
Cannot use spaces: my var (invalid)
Cannot use special characters: my@var (invalid)
Cannot be a reserved keyword: class, def, if, etc.

28. What are reserved keywords?
Words that Python reserves for its use.
Examples: if, else, for, while, def, class, import, return, True, False

29. What is the difference between local and global variables?
Local variables: defined inside a function, can only be used inside that function
Global variables: defined outside functions, can be used anywhere

30. What is variable naming convention?
Snake_case: my_variable (recommended for Python)
camelCase: myVariable
PascalCase: MyVariable
UPPER_CASE: MY_CONSTANT

=== PRACTICE QUESTIONS ===

31. Write a program to add two numbers.
x = 10
y = 20
sum = x + y
print(sum)

32. Write a program to swap two variables.
a = 5
b = 10
a, b = b, a
print(a, b)  # 10 5

33. Write a program to calculate area of circle.
import math
radius = 5
area = math.pi * radius ** 2
print(area)

34. Write a program to convert temperature from Celsius to Fahrenheit.
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)

35. Write a program to check if a number is even or odd.
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
