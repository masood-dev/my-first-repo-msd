# f-strings are used instead of normal casting, staring with 'f'. the expressions can be evalute using curly brackets.
"""
num = 3000
fraction = 1/3

print(f'{num*fraction} is {fraction*100}% of {num}')
---------
def greet(name):
    return(f"Hello {name}, welcome.")

x = input("enter your name: ")
user_name = greet(x)
print(user_name)

y = input("enter name nat: ")
nat = greet(y)
print(nat)
"""
'''
secret = 9

try:
    guess = int(input("guess the numb: "))

    if secret > guess:
        print("your guess is too low")
    elif secret < guess:
        print("your guess is too high")
    else:
        print("you got it.")
except ValueError:
    print("Please enter a valid number.")

    '''
'''
num = int(input('enter numb:' ))
while num > 0:
    print("Hello")
    num = num-1

n = 0

where = input("go left or right? ")
while where != "right":
    n = n + 1
    where = input("go left or right? ")
print("you got out!")
'''
'''
mysum = 0
start = 3
end = 5
for i in range(start, end):
    mysum += i
print(mysum)
'''
'''
#finds factorial
num = int(input("enter even if you want even or odd: "))
for i in range(0, 20+1, 2):
    print(i)
'''
'''
# Budget calculation
budgets = []
categories = ['twenty', 'thirty', 'fourty', 'eight', 'two']

for category in categories:
    value = float(input(f'Enter budget for {category}: '))
    budgets.append(value)

total_budget = sum(budgets)
average_budget = total_budget / 100
print(f'Total budget is ${average_budget:,.2f}')
'''

# ==================== FOR LOOP EXAMPLES - 6 LEVELS ====================

# LEVEL 1: BEGINNER - Simple iteration over a range

# Print numbers from 1 to 5
'''
for i in range(1, 6):
    print(i)
'''

# LEVEL 2: AFTER BASICS - Iterating over collections with simple operations

# Calculate sum of list elements
'''
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    print("num", num)
    total += num
print(f"Total: {total}")
'''
# Iterate over string characters
'''
word = "Python"
for char in word:
   print(f"Letter: {char}")


# LEVEL 3: INTERMEDIATE - Nested loops and enumerate

# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
'''
# Using enumerate for index and value
'''
fruits = ["apple", "banana", "cherry", "date"]
for egg, fruit in enumerate(fruits, start=1):
    print(f"{egg}. {fruit.capitalize()}")
'''

# LEVEL 4: SENIOR INTERMEDIATE - List comprehensions and zip

'''
# List comprehension with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
print(f"Squares of even numbers: {squares_of_evens}")


# Zip multiple lists together
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
'''

# Dictionary iteration with items()
student_scores = ["Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95]
for student, score in student_scores.items():
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"{student}: {score} ({grade})")
     