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