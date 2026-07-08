#learn this funtion in detail, what is this function's flow
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


#learn classes shit
#__init__ shit
#inheritance shit
#"self." shit
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


#learn god-damn list comprehension
#.items() shit and some other useful but important shit functions and methods


def factorial(n):
    """Calculate the factorial of a number"""
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example: factorial of 5
number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}")
print(f"{number}! = {number}*4*3*2*1 = {result}")

# Test with more numbers
for num in [0, 1, 3, 5, 7, 10]:
    print(f"{num}! = {factorial(num)}")