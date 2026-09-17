"""
Functions Interview Questions and Answers

1. What is the difference between parameters and arguments?
Parameters are variables defined in the function definition.
Example: def add(a, b):
Here, a and b are parameters.
Arguments are the actual values passed to the function when calling it.
Example: add(3, 5)
Here, 3 and 5 are arguments.

2. What is the difference between return and print?
print() displays output on the screen, but does not send data back to the caller.
return sends a value back from the function to where it was called.
Example:
def add(a, b):
    return a + b
result = add(2, 3)
print(result)  # prints 5

3. What is the difference between *args and **kwargs?
*args is used to pass a variable number of positional arguments to a function.
Example: def demo(*args):
    print(args)

demo(1, 2, 3)

**kwargs is used to pass a variable number of keyword arguments.
Example: def demo(**kwargs):
    print(kwargs)

demo(name='Alice', age=25)

4. What is recursion?
Recursion is when a function calls itself.
It is useful for problems like factorial, Fibonacci, and tree traversal.
Example:
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

5. What is a lambda function?
A lambda function is a small anonymous function defined in one line.
It is often used for short operations.
Example:
square = lambda x: x * x
print(square(5))  # 25

6. What is variable scope?
Variable scope refers to where a variable can be accessed in the program.
Local variables are defined inside a function and can only be used there.
Global variables are defined outside a function and are accessible everywhere.
Example:
count = 10  # global

def show():
    x = 5  # local
    print(count, x)

7. What are nested functions?
Nested functions are functions defined inside another function.
They are used when a helper function is only needed inside the outer function.
Example:
def outer():
    def inner():
        print('Hello from inner function')
    inner()

outer()

8. Why do we use functions?
Functions help in organizing code, reusing logic, and making programs easier to understand and maintain.
They reduce repetition and improve readability.

9. What is the difference between a function definition and function call?
A function definition creates the function body.
Example: def greet():
A function call executes the function.
Example: greet()

10. Can a function return multiple values?
Yes, a Python function can return multiple values as a tuple.
Example:
def info():
    return 'Alice', 25
name, age = info()

"""