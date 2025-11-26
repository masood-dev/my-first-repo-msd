print("hello world, this is my first repo.")
name=input("enter your name : ")
print("Your name is " + name + " and welcome " + name + '!')

# Simple function to greet a user
def greet_user(name):
	return f"Hey, {name}! how are you!"

# Example usage of the function
username = input("Enter your name: ")
# Store the result of the greet_user function in greeting
greeting = greet_user(username)
print(greeting)
