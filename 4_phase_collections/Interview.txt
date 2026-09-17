"""
Interview Questions and Answers on Python Collections

1. What is the difference between a list and a tuple?
A list is mutable, meaning its elements can be changed after creation.
Example: my_list = [1, 2, 3]; my_list.append(4)
A tuple is immutable, meaning it cannot be changed once created.
Example: my_tuple = (1, 2, 3)
Lists are used when data changes often, while tuples are used for fixed data.

2. Why are tuples immutable?
Tuples are immutable because they are designed to store fixed data safely.
This helps prevent accidental changes and can make programs more reliable.
It also allows tuples to be used as dictionary keys in some cases.

3. What is the difference between append() and extend()?
append() adds one element to the end of a list.
Example: numbers = [1, 2]; numbers.append(3) -> [1, 2, 3]
extend() adds multiple elements from another iterable.
Example: numbers.extend([4, 5]) -> [1, 2, 3, 4, 5]

4. What is the difference between remove() and pop()?
remove() deletes the first matching value from the list.
Example: numbers = [10, 20, 30]; numbers.remove(20)
pop() removes and returns an element at a specific index.
Example: numbers.pop(0) removes the first element and returns it.
If no index is given, pop() removes the last element.

5. What is the difference between sort() and sorted()?
sort() sorts a list in place and changes the original list.
Example: nums.sort() changes nums directly.
sorted() returns a new sorted list and does not modify the original list.
Example: new_nums = sorted(nums)

6. What is the difference between a dictionary and a set?
A dictionary stores data as key-value pairs.
Example: student = {'name': 'Alice', 'age': 22}
A set stores only unique values without any key-value mapping.
Example: colors = {'red', 'blue', 'green'}

7. Why are dictionary keys unique?
Dictionary keys must be unique because each key maps to exactly one value.
If a key is repeated, the latest value replaces the previous one.
Example: d = {'a': 1, 'a': 2} -> {'a': 2}

8. What is the difference between get() and [] in a dictionary?
dict[key] returns the value if the key exists; otherwise, it raises a KeyError.
Example: d['name'] -> 'Alice'
dict.get(key) returns the value if it exists, otherwise returns a default value or None.
Example: d.get('age', 0) -> 22 or 0 if missing

9. What is the difference between union() and intersection()?
union() combines two sets and returns all unique elements from both sets.
Example: {1, 2, 3}.union({3, 4}) -> {1, 2, 3, 4}
intersection() returns only the common elements present in both sets.
Example: {1, 2, 3}.intersection({3, 4}) -> {3}

10. When would you choose a set instead of a list?
Use a set when you need to store unique elements and perform fast membership checks.
Example: if 'apple' in fruits_set is very fast.
Lists are better when order matters and duplicate values are allowed.
Example: shopping_list = ['milk', 'bread', 'milk']

Example Usage:
my_list = [1, 2, 3]
my_list.append(4)
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {'name': 'John', 'age': 25}

print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)
"""
