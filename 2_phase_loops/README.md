# Phase 2: Loops and Control Flow

## Overview
This phase teaches you how to control program flow using loops and conditional statements. Learn to repeat code blocks and make decisions based on conditions.

## Learning Objectives
- Master `if`, `elif`, `else` statements
- Understand `for` loops and their uses
- Learn `while` loops and loop control
- Use `break`, `continue`, and `pass` statements
- Write nested loops and conditionals

## Key Concepts

### If-Else Statements
Make decisions in your code based on conditions.
```python
age = 20
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

### For Loops
Repeat a block of code for a fixed number of times or through a sequence.
```python
for i in range(5):
    print(i)

for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

### While Loops
Repeat a block while a condition is true.
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control Statements
- **break**: Exit the loop immediately
- **continue**: Skip the current iteration
- **pass**: Do nothing (placeholder)

```python
for i in range(10):
    if i == 5:
        break  # Exit loop
    print(i)
```

## How to Run
```bash
cd /Users/kanha/DevOps/python-practice/python_practice
source .venv/bin/activate
python 2_phase_loops.py
```

## Practice Exercises
1. Print numbers 1 to 10 using a for loop
2. Create a program to check if a number is prime
3. Print multiplication table using nested loops
4. Find sum of numbers from 1 to 100
5. Create a simple menu-driven program using loops

## Common Patterns
```python
# Sum of numbers
total = 0
for i in range(1, 11):
    total += i
print(total)

# Count occurrences
count = 0
for item in [1, 2, 1, 3, 1]:
    if item == 1:
        count += 1
print(count)
```

## Interview Tips
- Know the difference between for and while loops
- Understand when to use break and continue
- Be able to write nested loops efficiently
- Optimize loops for performance

## Next Phase
Move on to Phase 3 to learn about strings and string manipulation.
