Interview Questions and Answers on Python Strings

1. What is the difference between indexing and slicing?
Indexing accesses a single character at a specific position in a string.
Example: name[0] -> 'P'
Slicing extracts a part of the string using start and end indexes.
Example: name[0:4] -> 'Pyth'

2. Why are strings immutable?
Strings are immutable because once created, their contents cannot be changed.
If we try to modify a character, Python creates a new string instead of changing the original.
Example: s = 'hello'; s = 'H' + s[1:] -> creates a new string

3. What is the difference between find() and index()?
find() returns the index of the first occurrence of a substring, or -1 if not found.
Example: text.find('py') -> 0
index() also returns the index, but raises a ValueError if the substring is not found.
Example: text.index('py') -> 0

4. What is the difference between split() and join()?
split() breaks a string into a list of smaller strings based on a separator.
Example: 'a,b,c'.split(',') -> ['a', 'b', 'c']
join() does the opposite: it combines a list of strings into one string using a separator.
Example: ','.join(['a', 'b', 'c']) -> 'a,b,c'

5. Why do we use raw strings?
Raw strings are used when we want backslashes to be treated literally instead of as escape characters.
Example: print(r'C:\new\folder') keeps the backslashes as written.
This is useful in regex and file paths.

6. What is Unicode?
Unicode is a universal character encoding standard that represents most of the world’s written scripts.
It assigns a unique number to each character, such as letters, symbols, and emojis.

7. What is UTF-8 encoding?
UTF-8 is a variable-length encoding used to store Unicode characters in bytes.
It uses 1 byte for ASCII characters and more bytes for other characters.
It is widely used because it is compact and compatible with ASCII.

8. Why are f-strings preferred over .format()?
f-strings are easier to read and write.
They allow direct insertion of variables inside strings using curly braces.
Example: name = 'Alice'; print(f'Hello, {name}!')
This is more readable and cleaner than .format().

9. How does negative indexing work?
Negative indexing starts from the end of the string.
-1 refers to the last character, -2 to the second last character, and so on.
Example: word = 'python'; word[-1] -> 'n'; word[-3] -> 'h'

10. How do you reverse a string?
You can reverse a string using slicing with step -1.
Example: text = 'python'; reversed_text = text[::-1] -> 'nohtyp'
This works because slicing with -1 means go backward one step at a time.

Extra Example:
name = 'Python'
print(name[0])         # P
print(name[1:4])       # yth
print(name[-1])        # n
print(name[::-1])      # nohtyP
