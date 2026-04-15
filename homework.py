"""
PYTHON FUNCTIONS - HOMEWORK
Topic: Functions (Easy to Medium Level)
Complete all tasks below. Test your code to verify it works!
"""

# ============================================================================
# SECTION 1: BASIC FUNCTIONS (Easy)
# ============================================================================

# Task 1: Create a function that greets a person
# Function name: greet
# Parameter: name
# Return: "Hello, {name}!"
# Example: greet("Alice") → "Hello, Alice!"

# YOUR CODE HERE:
def greet(name):
    return f" hello, {name}"

greet("masood")



# Task 2: Create a function that calculates the area of a rectangle
# Function name: rectangle_area
# Parameters: length, width
# Return: area (length * width)
# Example: rectangle_area(5, 3) → 15

# YOUR CODE HERE:
def rectangle_area(length, width):
    return length * width

rectangle_area(5, 3)



# Task 3: Create a function that checks if a number is even
# Function name: is_even
# Parameter: number
# Return: True if even, False if odd
# Example: is_even(4) → True, is_even(7) → False

# YOUR CODE HERE:

#you tell me which version is better and more pythonic.

#version_1
def if_even(num):
    if num % 2 == 0:
        print(f"{num} is even!")
    else:
        print(f"{num} is not even!")

if_even(22)

#version_2
def is_even(num):
    num = num % 2 == 0
    return True if num else False

is_even(10)

# ============================================================================
# SECTION 2: DEFAULT PARAMETERS (Easy-Medium)
# ============================================================================

# Task 4: Create a function that calculates power with default exponent
# Function name: power
# Parameters: base, exponent=2 (default value)
# Return: base raised to the power of exponent
# Example: power(3) → 9, power(3, 3) → 27

# YOUR CODE HERE:
def power(base, exponent=2):
    return base ** exponent

power(3,3)



# Task 5: Create a coffee order function with default values
# Function name: order_coffee
# Parameters: size="medium", sugar=1, milk=True
# Return: A string describing the order
# Example: order_coffee() → "Medium coffee with 1 sugar and milk"

# YOUR CODE HERE:
def order_coffee(size="medium", sugar=1, milk=True):
    return f"{size} coffee with {sugar} sugar and milk"

order_coffee()



# ============================================================================
# SECTION 3: MULTIPLE RETURN VALUES (Medium)
# ============================================================================

# Task 6: Create a function that returns both quotient and remainder
# Function name: divide_with_remainder
# Parameters: dividend, divisor
# Return: tuple of (quotient, remainder)
# Example: divide_with_remainder(17, 5) → (3, 2)

# YOUR CODE HERE:
def divide_with_remainder(dividend, divisor):
    return dividend // divisor, dividend % divisor
    
divide_with_remainder(17, 5)



# Task 7: Create a function that finds min and max in a list
# Function name: find_min_max
# Parameter: numbers (list)
# Return: tuple of (minimum, maximum)
# Example: find_min_max([3, 7, 1, 9, 2]) → (1, 9)

# YOUR CODE HERE:
def find_min_max(numbers):
    return min(numbers), max(numbers)

find_min_max([1,2,3,4,5,6,7,8,9])



# ============================================================================
# SECTION 4: *args - VARIABLE POSITIONAL ARGUMENTS (Medium)
# ============================================================================

# Task 8: Create a function that finds the average of any number of values
# Function name: calculate_average
# Parameters: *numbers
# Return: average of all numbers
# Example: calculate_average(10, 20, 30) → 20.0

# YOUR CODE HERE:
def count_params(*args):
    return sum(args) / len(args)

print(count_params(10, 20, 30))



# Task 9: Create a function that finds the largest number from any amount of arguments
# Function name: find_maximum
# Parameters: *numbers
# Return: the largest number
# Example: find_maximum(5, 12, 3, 8, 15, 1) → 15

# YOUR CODE HERE:
def find_maximum(*numbers):
    return max(numbers)

print(find_maximum([1,2,3,4,5,50,47,40,500]))



# Task 10: Create a function that concatenates any number of strings with a space
# Function name: join_words
# Parameters: *words
# Return: all words joined with spaces
# Example: join_words("Hello", "World", "Python") → "Hello World Python"

# YOUR CODE HERE:
def join_words(*words):
    for word in words:
        print(word, end=' ')

join_words("hello", "world")



# ============================================================================
# SECTION 5: **kwargs - VARIABLE KEYWORD ARGUMENTS (Medium)
# ============================================================================

# Task 11: Create a function that builds a user profile
# Function name: create_profile
# Parameters: **info
# Return: formatted string with all info
# Example: create_profile(name="John", age=25, city="NYC") 
#          → "name: John, age: 25, city: NYC"

# YOUR CODE HERE:
def user_profile(**kwars):
    return kwars

print(user_profile(name="masood", age=21, gender="male"))



# Task 12: Create a function that counts how many keyword arguments were passed
# Function name: count_params
# Parameters: **kwargs
# Return: number of parameters passed
# Example: count_params(a=1, b=2, c=3) → 3

# YOUR CODE HERE:
def count_params(**kwargs):
    return len(kwargs)

print(count_params(a=1, b=2, c=3))



# ============================================================================
# SECTION 6: COMBINING *args AND **kwargs (Medium)
# ============================================================================

# Task 13: Create a flexible calculator function
# Function name: calculator
# Parameters: operation, *numbers, **options
# operation: "add", "multiply", "subtract"
# options: can include "round" (bool), "absolute" (bool)
# Return: result of operation
# Example: calculator("add", 5, 10, 15) → 30

# YOUR CODE HERE:
def calculator(operation, *numbers):
    result = False
    temp_mul = 1 
    if operation == "add":
        result = sum(numbers)
    elif operation == "mul":
        for i in numbers:
            temp_mul = i * temp_mul
        result = temp_mul
    elif operation == "sub":
        for i in numbers:
            result = i - result
    else:
        print("only three: addition, subtraction, multiplication can perform")
    print(round(result))

calculator("sub", 5, 10, 15)



# Task 14: Create a function that builds a product description
# Function name: product_info
# Parameters: *features, **details
# features: list of feature strings
# details: dict of detail key-value pairs
# Return: formatted string
# Example: product_info("Fast", "Reliable", name="Laptop", price=999)
#          → "Features: Fast, Reliable | Details: name=Laptop, price=999"

# YOUR CODE HERE:
def product_info(*features, **details):
    return f"Features: {features} | Details: {details}"

print(product_info("Fast", "Reliable", name="Laptop", price=999))



# ============================================================================
# SECTION 7: LAMBDA FUNCTIONS (Medium)
# ============================================================================

# Task 15: Create a lambda function that squares a number
# Variable name: square
# Example: square(5) → 25

# YOUR CODE HERE:
square = lambda x: x ** 2
print(square(5))



# Task 16: Create a lambda function that checks if a string length is > 5
# Variable name: is_long
# Example: is_long("Hello") → False, is_long("Python") → True

# YOUR CODE HERE:
is_long = lambda word: len(word) > 5 if True else False
print(is_long("pyt"))



# Task 17: Use lambda with filter to get even numbers from a list
# Given: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Create a list called 'evens' using filter and lambda

# YOUR CODE HERE:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [x**2 for x in numbers if print(x) else print('not even')]


# ============================================================================
# SECTION 8: PRACTICAL CHALLENGES (Medium)
# ============================================================================

# Task 18: Create a temperature converter
# Function name: convert_temperature
# Parameters: value, from_unit="C", to_unit="F"
# Supports: "C" (Celsius), "F" (Fahrenheit)
# Formulas: F = C * 9/5 + 32, C = (F - 32) * 5/9
# Return: converted temperature
# Example: convert_temperature(0, "C", "F") → 32.0

# YOUR CODE HERE:
def convert_temperature(value, from_unit='C', to_unit='F'):
    F = value * 9/5 + 32
    C = (F - 32) * 5/9
    return F

print(convert_temperature(100, 'C', 'F'))



# Task 19: Create a function that validates a password
# Function name: validate_password
# Parameter: password (string)
# Rules: at least 8 characters, has uppercase, has lowercase, has digit
# Return: True if valid, False otherwise

# YOUR CODE HERE:
# -- sorry i failed to get this right. --
def validate_password(string):
    password = ""
    if len(string) > 8:
        for char in string:
            if char in char.upper():
                password = password + char
            elif char in char.lower():
                password = password + char
            elif char is int():
                password = password + char
            else:
                print("not ok")
        print(password)
    else:
        print("not 8 chars")

validate_password("Mubashira1")



# Task 20: Create a function that generates a simple invoice
# Function name: generate_invoice
# Parameters: *items, **discounts
# items: tuples of (item_name, price)
# discounts: optional discount_percent=10
# Return: dictionary with 'subtotal', 'discount', 'total'
# Example: generate_invoice(("Laptop", 1000), ("Mouse", 50), discount_percent=10)
#          → {'subtotal': 1050, 'discount': 105, 'total': 945}

# YOUR CODE HERE:
def generate_invoice(*items, **discounts):
    
    subtotal = sum(item[1] for item in items)
    
    discount_percent = discounts.get('discount_percent', 0)
    
    discount_amount = subtotal * (discount_percent / 100)
    
    total = subtotal - discount_amount
    
    return {
        'subtotal': subtotal,
        'discount': discount_amount,
        'total': total
    }

print(generate_invoice(("Laptop", 1000), ("Mouse", 50), discount_percent=10))



# ============================================================================
# BONUS CHALLENGE: Combine everything you learned!
# ============================================================================

# Task 21: Create a flexible data processor
# Function name: process_data
# Parameters: data (list), operation="sum", *args, **kwargs
# Operations: "sum", "average", "filter_above", "filter_below"
# For filter operations, use kwargs: threshold=value
# Return: processed result
# Examples: 
#   process_data([1,2,3,4,5], "sum") → 15
#   process_data([1,2,3,4,5], "filter_above", threshold=3) → [4, 5]

# YOUR CODE HERE:
def process_data(data, operation="sum", *args, **kwargs):
    if operation == "sum":
        return sum(data)
    elif operation == "average":
        return sum(data) / len(data) if data else 0
    elif operation == "filter_above":
        threshold = kwargs.get("threshold", 0)
        return [x for x in data if x > threshold]
    elif operation == "filter_below":
        threshold = kwargs.get("threshold", 0)
        return [x for x in data if x < threshold]
    else:
        return "Invalid operation"

print(process_data([1, 2, 3, 4, 5], "sum"))
print(process_data([1, 2, 3, 4, 5], "filter_above", threshold=3))



# ============================================================================
# TEST YOUR FUNCTIONS BELOW
# ============================================================================

print("=" * 50)
print("TEST YOUR FUNCTIONS HERE")
print("=" * 50)

# Example tests (uncomment and modify as needed):
# print(greet("Student"))
# print(rectangle_area(10, 5))
# print(is_even(8))
# print(calculate_average(5, 10, 15, 20))



#=====================================================================

# PYTHON WARM-UP PROBLEMS FOR BEGINNERS
# Solve each problem below

# ============== PROBLEM 1 ==============
# Write a program to print "Hello, World!"



# ============== PROBLEM 2 ==============
# Take two numbers as input and print their sum
# Example: If user enters 5 and 3, output should be 8



# ============== PROBLEM 3 ==============
# Check if a number is even or odd
# Take a number as input and print "Even" or "Odd"



# ============== PROBLEM 4 ==============
# Find the largest of three numbers
# Take three numbers as input and print the largest one



# ============== PROBLEM 5 ==============
# Print all numbers from 1 to 10



# ============== PROBLEM 6 ==============
# Print all even numbers from 1 to 20



# ============== PROBLEM 7 ==============
# Calculate the factorial of a number
# Example: factorial of 5 is 5*4*3*2*1 = 120



# ============== PROBLEM 8 ==============
# Print the multiplication table of a number
# Example: For 5, print 5*1=5, 5*2=10, ... 5*10=50



# ============== PROBLEM 9 ==============
# Reverse a string
# Example: "hello" should become "olleh"



# ============== PROBLEM 10 ==============
# Count vowels in a string
# Example: "hello" has 2 vowels (e, o)



# ============== PROBLEM 11 ==============
# Check if a string is palindrome
# Example: "racecar" is palindrome, "hello" is not



# ============== PROBLEM 12 ==============
# Find sum of all numbers in a list
# Example: [1, 2, 3, 4, 5] → sum is 15



# ============== PROBLEM 13 ==============
# Find the maximum number in a list (without using max())
# Example: [3, 7, 2, 9, 1] → maximum is 9



# ============== PROBLEM 14 ==============
# Remove duplicates from a list
# Example: [1, 2, 2, 3, 4, 4, 5] → [1, 2, 3, 4, 5]



# ============== PROBLEM 15 ==============
# Count the number of words in a sentence
# Example: "Hello World" → 2 words



# ============== PROBLEM 16 ==============
# Print first 10 Fibonacci numbers
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...



# ============== PROBLEM 17 ==============
# Convert Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32



# ============== PROBLEM 18 ==============
# Check if a number is prime
# Example: 7 is prime, 8 is not



# ============== PROBLEM 19 ==============
# Swap two variables without using a third variable



# ============== PROBLEM 20 ==============
# Print the pattern:
# *
# **
# ***
# ****
# *****
