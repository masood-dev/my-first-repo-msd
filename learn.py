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

x = 1
y = 6

while (x < y):
    print("you're right")
    x += 1