"""
PYTHON PROGRAMMING SYLLABUS - COMPLETE REFERENCE WITH EXAMPLES
================================================================
This file contains examples of all important Python topics organized by categories.
"""

# ============================================================================
# CATEGORY 1: DATA STRUCTURES
# ============================================================================

# ----------------------------------------------------------------------------
# 1.1 LISTS
# ----------------------------------------------------------------------------
"""
LISTS: Ordered, mutable (changeable) collection that allows duplicate elements.
Lists are defined using square brackets [].
Use cases: When you need an ordered collection that can be modified.
"""

# Example 1: Basic list operations
print("=== LISTS - Example 1 ===")
fruits = ["apple", "banana", "cherry", "date"]
print(f"Original list: {fruits}")

# Accessing elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Modifying lists
fruits.append("elderberry")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "apricot")  # Insert at position
print(f"After insert: {fruits}")

fruits.remove("banana")  # Remove specific element
print(f"After remove: {fruits}")

# List slicing
print(f"First 3 fruits: {fruits[:3]}")
print(f"Last 2 fruits: {fruits[-2:]}")

# Example 2: List comprehension and methods
print("\n=== LISTS - Example 2 ===")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension - create new list with condition
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Squared numbers
squared = [num ** 2 for num in numbers]
print(f"Squared: {squared}")

# Useful list methods
numbers_copy = numbers.copy()
numbers_copy.reverse()
print(f"Reversed: {numbers_copy}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}, Min: {min(numbers)}")
print(f"Length: {len(numbers)}")

# ----------------------------------------------------------------------------
# 1.2 SETS
# ----------------------------------------------------------------------------
"""
SETS: Unordered collection of unique elements. No duplicates allowed.
Sets are defined using curly braces {} or set() constructor.
Use cases: Remove duplicates, membership testing, mathematical set operations.
"""

# Example 1: Basic set operations
print("\n=== SETS - Example 1 ===")
# Creating sets
colors = {"red", "green", "blue", "red"}  # Duplicate 'red' will be removed
print(f"Colors set: {colors}")

# Adding and removing elements
colors.add("yellow")
print(f"After add: {colors}")

colors.discard("green")  # Doesn't raise error if element doesn't exist
print(f"After discard: {colors}")

# Membership testing (very fast in sets)
print(f"Is 'red' in colors? {'red' in colors}")

# Example 2: Set mathematical operations
print("\n=== SETS - Example 2 ===")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union - all elements from both sets
union = set_a | set_b  # or set_a.union(set_b)
print(f"Union: {union}")

# Intersection - common elements
intersection = set_a & set_b  # or set_a.intersection(set_b)
print(f"Intersection: {intersection}")

# Difference - elements in set_a but not in set_b
difference = set_a - set_b  # or set_a.difference(set_b)
print(f"Difference (A-B): {difference}")

# Symmetric difference - elements in either set but not both
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(f"Symmetric difference: {sym_diff}")

# ----------------------------------------------------------------------------
# 1.3 TUPLES
# ----------------------------------------------------------------------------
"""
TUPLES: Ordered, immutable (unchangeable) collection that allows duplicates.
Tuples are defined using parentheses () or just comma-separated values.
Use cases: When you need data that shouldn't be modified, returning multiple values.
"""

# Example 1: Basic tuple operations
print("\n=== TUPLES - Example 1 ===")
coordinates = (10, 20, 30)
print(f"Coordinates: {coordinates}")

# Accessing elements
print(f"X coordinate: {coordinates[0]}")

# Tuples are immutable - this would cause an error:
# coordinates[0] = 15  # TypeError!

# Tuple unpacking
x, y, z = coordinates
print(f"Unpacked: x={x}, y={y}, z={z}")

# Tuple methods
numbers_tuple = (1, 2, 2, 3, 2, 4, 5)
print(f"Count of 2: {numbers_tuple.count(2)}")
print(f"Index of 3: {numbers_tuple.index(3)}")

# Example 2: Tuples as return values and in data structures
print("\n=== TUPLES - Example 2 ===")
def get_user_info():
    """Function returning multiple values as tuple"""
    name = "Alice"
    age = 25
    city = "New York"
    return name, age, city  # Returns a tuple

# Unpacking returned tuple
user_name, user_age, user_city = get_user_info()
print(f"User: {user_name}, {user_age}, {user_city}")

# List of tuples (common pattern)
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]
for name, score in students:
    print(f"{name}: {score}")

# ----------------------------------------------------------------------------
# 1.4 DICTIONARIES
# ----------------------------------------------------------------------------
"""
DICTIONARIES: Unordered collection of key-value pairs. Keys must be unique.
Dictionaries are defined using curly braces {} with key:value pairs.
Use cases: Storing related data, fast lookup by key, JSON-like structures.
"""

# Example 1: Basic dictionary operations
print("\n=== DICTIONARIES - Example 1 ===")
student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "Chemistry"]
}
print(f"Student: {student}")

# Accessing values
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")  # Safer - returns None if key doesn't exist

# Adding/modifying entries
student["email"] = "john@example.com"
student["age"] = 21
print(f"Updated student: {student}")

# Removing entries
removed_grade = student.pop("grade")
print(f"Removed grade: {removed_grade}")

# Example 2: Dictionary methods and iteration
print("\n=== DICTIONARIES - Example 2 ===")
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

# Iterating through dictionary
print("Inventory:")
for item, quantity in inventory.items():
    print(f"  {item}: {quantity}")

# Dictionary methods
print(f"Keys: {list(inventory.keys())}")
print(f"Values: {list(inventory.values())}")

# Dictionary comprehension
prices = {"apples": 0.5, "bananas": 0.3, "oranges": 0.6}
total_values = {item: inventory[item] * prices[item] for item in inventory}
print(f"Total values: {total_values}")

# Merging dictionaries (Python 3.9+)
combined = inventory | prices  # or {**inventory, **prices}
print(f"Combined: {combined}")

# ============================================================================
# CATEGORY 2: CONTROL FLOW
# ============================================================================

# ----------------------------------------------------------------------------
# 2.1 CONDITIONAL STATEMENTS (if, elif, else)
# ----------------------------------------------------------------------------
"""
CONDITIONAL STATEMENTS: Execute different code blocks based on conditions.
Syntax: if condition:, elif condition:, else:
Use cases: Decision making, branching logic, input validation.
"""

# Example 1: Basic if-elif-else
print("\n=== CONDITIONALS - Example 1 ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Ternary operator (one-line if-else)
status = "Pass" if score >= 60 else "Fail"
print(f"Status: {status}")

# Example 2: Complex conditions
print("\n=== CONDITIONALS - Example 2 ===")
age = 25
has_license = True
has_insurance = True

# Multiple conditions with and, or, not
if age >= 18 and has_license and has_insurance:
    print("You can rent a car")
elif age >= 18 and has_license:
    print("You need insurance to rent a car")
elif age >= 18:
    print("You need a license and insurance")
else:
    print("You must be 18 or older")

# Checking membership
allowed_users = ["alice", "bob", "charlie"]
username = "alice"
if username in allowed_users:
    print(f"{username} is authorized")

# ----------------------------------------------------------------------------
# 2.2 LOOPS (for, while)
# ----------------------------------------------------------------------------
"""
LOOPS: Repeat code blocks multiple times.
FOR loop: Iterate over sequences (lists, strings, ranges, etc.)
WHILE loop: Repeat while a condition is true
"""

# Example 1: For loops
print("\n=== LOOPS - Example 1 (for) ===")
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Using range()
print("Counting:")
for i in range(1, 6):  # 1 to 5
    print(i, end=" ")
print()

# Enumerate - get index and value
print("Indexed fruits:")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Example 2: While loops and loop control
print("\n=== LOOPS - Example 2 (while) ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Break and continue
print("Finding first even number:")
numbers = [1, 3, 5, 8, 9, 10, 11]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break  # Exit loop
    print(f"{num} is odd")

print("Skip multiples of 3:")
for num in range(1, 11):
    if num % 3 == 0:
        continue  # Skip to next iteration
    print(num, end=" ")
print()

# ============================================================================
# CATEGORY 3: FUNCTIONS
# ============================================================================

# ----------------------------------------------------------------------------
# 3.1 FUNCTION BASICS
# ----------------------------------------------------------------------------
"""
FUNCTIONS: Reusable blocks of code that perform specific tasks.
Defined using 'def' keyword.
Can accept parameters and return values.
Use cases: Code reusability, organization, modularity.
"""

# Example 1: Basic functions with parameters and return values
print("\n=== FUNCTIONS - Example 1 ===")

def greet(name):
    """Simple function with one parameter"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Function with multiple parameters"""
    return a + b

def calculate_area(length, width):
    """Function with multiple parameters and calculation"""
    area = length * width
    return area

# Calling functions
print(greet("Alice"))
print(f"5 + 3 = {add_numbers(5, 3)}")
print(f"Area: {calculate_area(10, 5)}")

# Example 2: Advanced function features
print("\n=== FUNCTIONS - Example 2 ===")

def power(base, exponent=2):
    """Function with default parameter"""
    return base ** exponent

print(f"3^2 = {power(3)}")  # Uses default exponent=2
print(f"3^3 = {power(3, 3)}")  # Override default

def summarize(*args, **kwargs):
    """Function with variable arguments
    *args: variable positional arguments (tuple)
    **kwargs: variable keyword arguments (dictionary)
    """
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    return sum(args) if args else 0

total = summarize(1, 2, 3, 4, 5, name="Test", operation="sum")
print(f"Total: {total}")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(f"4 * 6 = {multiply(4, 6)}")

# ----------------------------------------------------------------------------
# 3.2 SCOPE AND RECURSION
# ----------------------------------------------------------------------------
"""
SCOPE: Defines where variables are accessible (global vs local).
RECURSION: Function calling itself to solve problems.
"""

# Example 1: Scope
print("\n=== SCOPE - Example 1 ===")

global_var = "I'm global"

def scope_demo():
    local_var = "I'm local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

scope_demo()
print(f"Outside function: {global_var}")
# print(local_var)  # Would cause error - local_var not accessible here

# Example 2: Recursion
print("\n=== RECURSION - Example 2 ===")

def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

def fibonacci(n):
    """Generate nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("First 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()

# ============================================================================
# CATEGORY 4: MODULES AND PACKAGES
# ============================================================================

# ----------------------------------------------------------------------------
# 4.1 IMPORTING MODULES
# ----------------------------------------------------------------------------
"""
MODULES: Python files containing functions, classes, and variables.
Modules help organize code and promote reusability.
Import using: import, from...import, import...as
"""

# Example 1: Different ways to import
print("\n=== MODULES - Example 1 ===")

# Method 1: Import entire module
import math
print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# Method 2: Import specific items
from math import ceil, floor
print(f"Ceil of 4.3: {ceil(4.3)}")
print(f"Floor of 4.7: {floor(4.7)}")

# Method 3: Import with alias
import datetime as dt
now = dt.datetime.now()
print(f"Current time: {now}")

# Example 2: Using various standard library modules
print("\n=== MODULES - Example 2 ===")

import random
import os
from collections import Counter

# Random module
numbers = [random.randint(1, 10) for _ in range(5)]
print(f"Random numbers: {numbers}")
print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")

# OS module
print(f"Current directory: {os.getcwd()}")

# Collections module
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
word_count = Counter(words)
print(f"Word count: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# ----------------------------------------------------------------------------
# 4.2 CREATING MODULES
# ----------------------------------------------------------------------------
"""
CREATING MODULES: Any Python file can be a module.
Save functions in a .py file and import them in other files.
"""

# Example 1: Module structure (conceptual)
print("\n=== CREATING MODULES - Example 1 ===")
"""
To create a module:
1. Create a file, e.g., 'my_math.py':
   
   def add(a, b):
       return a + b
   
   def multiply(a, b):
       return a * b
   
   PI = 3.14159

2. Import and use in another file:
   
   import my_math
   result = my_math.add(5, 3)
   print(my_math.PI)
"""

# Example 2: Package structure
print("\n=== PACKAGES - Example 2 ===")
"""
PACKAGES: Directories containing multiple modules and an __init__.py file.

Package structure example:
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py

Usage:
    from my_package import module1
    from my_package.subpackage import module3
    
Common standard packages:
- os: Operating system interface
- sys: System-specific parameters
- json: JSON encoding/decoding
- re: Regular expressions
- datetime: Date and time handling
- collections: Additional data structures
"""

# ============================================================================
# CATEGORY 5: FILE HANDLING
# ============================================================================

# ----------------------------------------------------------------------------
# 5.1 READING AND WRITING FILES
# ----------------------------------------------------------------------------
"""
FILE HANDLING: Read from and write to files.
Modes: 'r' (read), 'w' (write), 'a' (append), 'r+' (read+write)
Always use 'with' statement for automatic file closing.
"""

# Example 1: Writing to files
print("\n=== FILE HANDLING - Example 1 (Writing) ===")

# Writing text to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file.writelines(lines)

print("File written successfully")

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("Appended line\n")

# Example 2: Reading from files
print("\n=== FILE HANDLING - Example 2 (Reading) ===")

# Reading entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Full content:")
    print(content)

# Reading line by line
print("Reading line by line:")
with open('example.txt', 'r') as file:
    for line_num, line in enumerate(file, 1):
        print(f"{line_num}: {line.strip()}")

# Reading all lines into a list
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")

# ============================================================================
# CATEGORY 6: ERROR HANDLING
# ============================================================================

# ----------------------------------------------------------------------------
# 6.1 TRY-EXCEPT BLOCKS
# ----------------------------------------------------------------------------
"""
ERROR HANDLING: Handle errors gracefully without crashing the program.
try: Code that might raise an error
except: Code to run if error occurs
else: Code to run if no error occurs
finally: Code that always runs
"""

# Example 1: Basic error handling
print("\n=== ERROR HANDLING - Example 1 ===")

def divide(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input types!")
        return None

divide(10, 2)
divide(10, 0)
divide(10, "2")

# Example 2: Advanced error handling
print("\n=== ERROR HANDLING - Example 2 ===")

def process_list(numbers, index):
    try:
        result = numbers[index] * 2
        print(f"Result: {result}")
        return result
    except IndexError:
        print(f"Error: Index {index} is out of range")
    except TypeError:
        print("Error: Invalid operation")
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        print("Operation successful!")
    finally:
        print("Cleanup completed")

my_list = [1, 2, 3, 4, 5]
process_list(my_list, 2)
print()
process_list(my_list, 10)

# ============================================================================
# CATEGORY 7: OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================================

# ----------------------------------------------------------------------------
# 7.1 CLASSES AND OBJECTS
# ----------------------------------------------------------------------------
"""
CLASSES: Blueprints for creating objects.
OBJECTS: Instances of classes.
Encapsulation: Bundling data and methods that work on that data.
"""

# Example 1: Basic class
print("\n=== OOP - Example 1 (Classes and Objects) ===")

class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Constructor - initialize instance variables"""
        self.name = name
        self.age = age
    
    def bark(self):
        """Instance method"""
        return f"{self.name} says Woof!"
    
    def get_info(self):
        """Return dog information"""
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())
print(dog2.get_info())
print(f"Species: {Dog.species}")

# Example 2: Inheritance and method overriding
print("\n=== OOP - Example 2 (Inheritance) ===")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Cat(Animal):
    """Cat inherits from Animal"""
    def speak(self):
        """Override parent method"""
        return f"{self.name} says Meow!"

class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)  # Call parent constructor
        self.can_fly = can_fly
    
    def speak(self):
        return f"{self.name} says Tweet!"

cat = Cat("Whiskers")
bird = Bird("Tweety")

print(cat.speak())
print(bird.speak())
print(f"Can {bird.name} fly? {bird.can_fly}")

# ============================================================================
# CATEGORY 8: STRING MANIPULATION
# ============================================================================

# ----------------------------------------------------------------------------
# 8.1 STRING METHODS AND FORMATTING
# ----------------------------------------------------------------------------
"""
STRINGS: Immutable sequences of characters.
Rich set of methods for manipulation and formatting.
"""

# Example 1: String methods
print("\n=== STRINGS - Example 1 (Methods) ===")

text = "  Hello, Python World!  "

print(f"Original: '{text}'")
print(f"Lower: '{text.lower()}'")
print(f"Upper: '{text.upper()}'")
print(f"Title: '{text.title()}'")
print(f"Strip: '{text.strip()}'")
print(f"Replace: '{text.replace('Python', 'Amazing')}'")

# String checking methods
print(f"Starts with 'Hello': {text.strip().startswith('Hello')}")
print(f"Ends with '!': {text.strip().endswith('!')}")
print(f"Contains 'Python': {'Python' in text}")

# Splitting and joining
words = text.strip().split()
print(f"Words: {words}")
print(f"Joined: {'-'.join(words)}")

# Example 2: String formatting
print("\n=== STRINGS - Example 2 (Formatting) ===")

name = "Alice"
age = 25
score = 95.567

# f-strings (Python 3.6+) - recommended
print(f"Name: {name}, Age: {age}, Score: {score:.2f}")

# Format method
print("Name: {}, Age: {}, Score: {:.2f}".format(name, age, score))

# String multiplication and concatenation
separator = "=" * 50
print(separator)
greeting = "Hello " + name
print(greeting)

# Multi-line strings
multiline = """
This is a
multi-line
string
"""
print(multiline)

# ============================================================================
# CATEGORY 9: LIST COMPREHENSIONS AND GENERATORS
# ============================================================================

# ----------------------------------------------------------------------------
# 9.1 COMPREHENSIONS
# ----------------------------------------------------------------------------
"""
COMPREHENSIONS: Concise way to create lists, sets, and dictionaries.
Syntax: [expression for item in iterable if condition]
"""

# Example 1: List comprehensions
print("\n=== COMPREHENSIONS - Example 1 (Lists) ===")

# Basic list comprehension
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# String comprehension
sentence = "Hello World"
vowels = [char for char in sentence if char.lower() in 'aeiou']
print(f"Vowels: {vowels}")

# Example 2: Dict and Set comprehensions
print("\n=== COMPREHENSIONS - Example 2 (Dict/Set) ===")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# Set comprehension
unique_lengths = {len(word) for word in ['apple', 'banana', 'cherry', 'date']}
print(f"Unique word lengths: {unique_lengths}")

# Conditional dict comprehension
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
high_scores = {name: score for name, score in scores.items() if score >= 85}
print(f"High scores: {high_scores}")

# ============================================================================
# CATEGORY 10: COMMON BUILT-IN FUNCTIONS
# ============================================================================

# ----------------------------------------------------------------------------
# 10.1 USEFUL BUILT-IN FUNCTIONS
# ----------------------------------------------------------------------------
"""
BUILT-IN FUNCTIONS: Python provides many useful functions out of the box.
No import needed - always available.
"""

# Example 1: Data analysis functions
print("\n=== BUILT-IN FUNCTIONS - Example 1 ===")

numbers = [45, 23, 67, 12, 89, 34, 56]

print(f"Numbers: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sorted: {sorted(numbers)}")
print(f"Reversed: {list(reversed(numbers))}")

# Any and all
conditions = [True, True, False, True]
print(f"All true? {all(conditions)}")
print(f"Any true? {any(conditions)}")

# Example 2: Type conversion and mapping
print("\n=== BUILT-IN FUNCTIONS - Example 2 ===")

# Type conversions
print(f"String to int: {int('42')}")
print(f"Int to string: {str(42)}")
print(f"String to float: {float('3.14')}")
print(f"List to tuple: {tuple([1, 2, 3])}")
print(f"String to list: {list('hello')}")

# Map function - apply function to all items
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(f"Mapped squares: {squared}")

# Filter function - filter items by condition
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filtered even: {even}")

# Zip function - combine iterables
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
combined = list(zip(names, scores))
print(f"Zipped: {combined}")

# ============================================================================
# CATEGORY 11: ADVANCED TOPICS
# ============================================================================

# ----------------------------------------------------------------------------
# 11.1 DECORATORS AND CONTEXT MANAGERS
# ----------------------------------------------------------------------------
"""
DECORATORS: Functions that modify other functions.
Syntax: @decorator_name above function definition.
"""

# Example 1: Simple decorator
print("\n=== DECORATORS - Example 1 ===")

def uppercase_decorator(func):
    """Decorator that converts result to uppercase"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet_person(name):
    return f"hello, {name}"

print(greet_person("alice"))

# Example 2: Practical decorator
print("\n=== DECORATORS - Example 2 ===")

def timer_decorator(func):
    """Decorator to measure execution time"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

result = slow_function()

# ----------------------------------------------------------------------------
# 11.2 REGULAR EXPRESSIONS
# ----------------------------------------------------------------------------
"""
REGULAR EXPRESSIONS: Pattern matching in strings.
Import 're' module to use regex.
"""

# Example 1: Basic regex patterns
print("\n=== REGULAR EXPRESSIONS - Example 1 ===")

import re

text = "Contact us at info@example.com or support@test.org"

# Find all emails
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(f"Emails found: {emails}")

# Search for pattern
phone = "Call me at 123-456-7890"
match = re.search(r'\d{3}-\d{3}-\d{4}', phone)
if match:
    print(f"Phone number: {match.group()}")

# Example 2: Replace and split
print("\n=== REGULAR EXPRESSIONS - Example 2 ===")

# Replace pattern
text = "The price is $100 and $200"
new_text = re.sub(r'\$(\d+)', r'USD \1', text)
print(f"Replaced: {new_text}")

# Split by pattern
sentence = "apple,banana;cherry|date"
fruits = re.split(r'[,;|]', sentence)
print(f"Split fruits: {fruits}")

# ============================================================================
# SUMMARY
# ============================================================================
"""
This syllabus covers:

1. DATA STRUCTURES: Lists, Sets, Tuples, Dictionaries
2. CONTROL FLOW: Conditionals, Loops
3. FUNCTIONS: Basic, Advanced, Scope, Recursion
4. MODULES & PACKAGES: Importing, Creating, Standard library
5. FILE HANDLING: Reading, Writing files
6. ERROR HANDLING: Try-except blocks
7. OOP: Classes, Objects, Inheritance
8. STRING MANIPULATION: Methods, Formatting
9. COMPREHENSIONS: List, Dict, Set comprehensions
10. BUILT-IN FUNCTIONS: Common utilities
11. ADVANCED TOPICS: Decorators, Regular expressions

Practice these examples and experiment with variations to master Python!
"""

print("\n" + "=" * 60)
print("END OF PYTHON SYLLABUS")
print("=" * 60)
