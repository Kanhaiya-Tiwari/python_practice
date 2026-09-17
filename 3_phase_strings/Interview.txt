PHASE 3: STRINGS AND STRING MANIPULATION - INTERVIEW QUESTIONS & ANSWERS

=== BASIC STRING CONCEPTS ===

1. What is a string?
A string is a sequence of characters enclosed in quotes.
Example: "Hello", 'World', """Multiple lines"""

2. What are the ways to create a string?
Single quotes: 'Hello'
Double quotes: "Hello"
Triple quotes (multi-line): """Hello World"""
Raw strings: r"C:\new\folder"

3. What is the difference between single and double quotes?
No practical difference in Python. Use based on convenience.
Use double quotes if string contains single quote: "It's"
Use single quotes if string contains double quote: 'Say "Hi"'

4. What are raw strings?
Strings where backslashes are treated literally.
Used for file paths and regex patterns.
Example: r"C:\new\folder" (backslash not escaped)

5. What is string immutability?
Strings cannot be changed once created.
Attempting to modify creates a new string.
Example: s = "hello"; s = "H" + s[1:] (creates new string)

6. Why are strings immutable?
For security and performance reasons
Allows strings to be used as dictionary keys
Prevents accidental modifications

7. What is the difference between string and list?
String: immutable sequence of characters
List: mutable sequence that can hold any type of data

8. What is the len() function?
Returns the number of characters in a string.
Example: len("Hello") returns 5

9. What is the type() function?
Returns the data type of a value.
Example: type("Hello") returns <class 'str'>

10. What is the difference between == and 'is' for strings?
== compares values
'is' compares if they refer to the same object
Example: "hello" == "hello" (True), "hello" is "hello" (usually True, but not guaranteed)

=== INDEXING & SLICING ===

11. What is indexing?
Accessing a single character at a specific position.
Example: name[0] returns first character
Indices start from 0

12. What is negative indexing?
Accessing characters from the end using negative indices.
Example: name[-1] returns last character
-2 returns second last, etc.

13. What is slicing?
Extracting a portion (substring) of a string.
Example: text[0:5] returns first 5 characters
text[start:end:step]

14. What is the difference between indexing and slicing?
Indexing: Access single character. Example: s[2] returns one character
Slicing: Access multiple characters. Example: s[1:4] returns substring

15. How do you reverse a string?
Using slicing with step -1.
Example: text[::-1] reverses the string

16. What is step in slicing?
Step determines which characters to include.
Example: text[::2] returns every 2nd character
text[::-1] returns every character in reverse (step of -1)

17. What is the difference between [start:end] and [start:end:step]?
[start:end] gets characters from start to end-1 with step 1
[start:end:step] gets characters with custom step size

18. What is the difference between "string"[0:3] and "string"[0:3:1]?
Both do the same thing. The step 1 is default if not specified.

19. Can you change a character in string using indexing?
No, strings are immutable.
Example: s[0] = 'A' will raise TypeError
Instead: s = 'A' + s[1:]

20. What is the difference between s[::] and s[:]?
Both return the entire string unchanged.
s[::] is equivalent to s[::]
s[:] is equivalent to s[0:len(s):1]

=== STRING METHODS ===

21. What is the find() method?
Searches for a substring and returns its index.
Returns -1 if not found.
Example: "hello".find("l") returns 2

22. What is the index() method?
Similar to find(), but raises ValueError if not found.
Example: "hello".index("l") returns 2

23. What is the difference between find() and index()?
find() returns -1 if substring not found
index() raises ValueError if substring not found
Both return the first occurrence

24. What is the count() method?
Counts how many times a substring appears.
Example: "banana".count("a") returns 3

25. What is the upper() method?
Converts all characters to uppercase.
Example: "hello".upper() returns "HELLO"

26. What is the lower() method?
Converts all characters to lowercase.
Example: "HELLO".lower() returns "hello"

27. What is the capitalize() method?
Converts first character to uppercase, rest to lowercase.
Example: "hELLO".capitalize() returns "Hello"

28. What is the title() method?
Converts first character of each word to uppercase.
Example: "hello world".title() returns "Hello World"

29. What is the strip() method?
Removes leading and trailing whitespace.
Example: "  hello  ".strip() returns "hello"

30. What is the difference between strip(), lstrip(), and rstrip()?
strip() removes from both sides
lstrip() removes from left side only
rstrip() removes from right side only

31. What is the replace() method?
Replaces all occurrences of a substring.
Example: "hello".replace("l", "L") returns "heLLo"

32. What is the split() method?
Breaks a string into a list of substrings.
Example: "a,b,c".split(",") returns ['a', 'b', 'c']

33. What is the join() method?
Combines a list of strings into a single string.
Example: "-".join(['a', 'b', 'c']) returns "a-b-c"

34. What is the difference between split() and join()?
split() breaks string into list (string → list)
join() combines list into string (list → string)
They are opposite operations

35. What is the startswith() method?
Checks if string starts with a substring.
Example: "hello".startswith("he") returns True

36. What is the endswith() method?
Checks if string ends with a substring.
Example: "hello".endswith("lo") returns True

37. What is the isdigit() method?
Checks if all characters are digits.
Example: "12345".isdigit() returns True

38. What is the isalpha() method?
Checks if all characters are alphabetic.
Example: "hello".isalpha() returns True

39. What is the isalnum() method?
Checks if all characters are alphanumeric (letters and digits).
Example: "hello123".isalnum() returns True

40. What is the isspace() method?
Checks if all characters are whitespace.
Example: "   ".isspace() returns True

=== STRING FORMATTING ===

41. What are the ways to format strings?
1. f-strings (modern, Python 3.6+)
2. .format() method
3. % operator (old style)
4. String concatenation

42. What are f-strings?
F-strings allow embedding variables directly.
Example: name = "Alice"; f"Hello {name}"
Supports expressions: f"2 + 2 = {2 + 2}"

43. What is the difference between f-strings and .format()?
f-strings are faster and more readable: f"{name}"
.format() is older: "{}".format(name)
f-strings support expressions: f"{x+5}"

44. What is the difference between f-strings and % formatting?
f-strings: f"Value is {x}"
%: "Value is %d" % x
f-strings are more readable and preferred

45. How do you format numbers in f-strings?
f"{x:.2f}" - 2 decimal places
f"{x:,}"    - add commas
f"{x:05d}"  - pad with zeros
Example: f"{3.14159:.2f}" returns "3.14"

46. What is string concatenation?
Combining strings using + operator.
Example: "Hello" + " " + "World" returns "Hello World"

47. When should you use f-strings over concatenation?
Always use f-strings. They are faster and cleaner.
Concatenation is slower because it creates intermediate strings.

48. How do you include special characters in f-strings?
Use escape sequences:
\n - newline
\t - tab
\\ - backslash
\" - double quote
\' - single quote

49. What is the format() method?
Formats string with placeholders {} replaced by arguments.
Example: "Hello {}".format("Alice")

50. What is tuple unpacking in format()?
"Hello {} {}".format("Alice", "Bob")
Or: "Hello {0} {1}".format("Alice", "Bob")

=== UNICODE & ENCODING ===

51. What is Unicode?
Universal character encoding standard representing characters worldwide.
Assigns unique number to each character.
Supports letters, symbols, emojis from all languages.

52. What is UTF-8?
Variable-length encoding for Unicode characters.
1 byte for ASCII, more bytes for other characters.
Most widely used for web and files.

53. How do you encode a string?
Using encode() method.
Example: "hello".encode('utf-8') returns b'hello'

54. How do you decode bytes?
Using decode() method.
Example: b'hello'.decode('utf-8') returns "hello"

55. What is the difference between encode() and decode()?
encode() converts string → bytes
decode() converts bytes → string
They are opposite operations

=== PRACTICE QUESTIONS ===

56. Write a program to count vowels in a string.
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(count)

57. Write a program to check if a string is palindrome.
text = "racecar"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

58. Write a program to remove duplicates from a string.
text = "aabbccdd"
result = ''.join(dict.fromkeys(text))
print(result)

59. Write a program to reverse words in a sentence.
sentence = "Hello World Python"
reversed_sentence = ' '.join(sentence.split()[::-1])
print(reversed_sentence)

60. Write a program to count frequency of each character.
text = "hello"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)
