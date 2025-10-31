# Example: Calculator Functions

"""
calculator.py - A simple calculator to demonstrate functions and documentation

This example shows:
- Function definitions
- Parameters and return values
- Documentation strings (docstrings)
- Basic arithmetic operations
"""


def add(a, b):
    """
    Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Sum of a and b
        
    Example:
        >>> add(2, 3)
        5.0
    """
    return a + b


def subtract(a, b):
    """
    Subtract b from a.
    
    Args:
        a (float): Number to subtract from
        b (float): Number to subtract
        
    Returns:
        float: Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide a by b.
    
    Args:
        a (float): Numerator
        b (float): Denominator
        
    Returns:
        float: Quotient of a divided by b
        
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


# Example usage
if __name__ == "__main__":
    print("Simple Calculator Examples")
    print("-" * 30)
    
    # Addition
    result = add(10, 5)
    print(f"10 + 5 = {result}")
    
    # Subtraction
    result = subtract(10, 5)
    print(f"10 - 5 = {result}")
    
    # Multiplication
    result = multiply(10, 5)
    print(f"10 * 5 = {result}")
    
    # Division
    result = divide(10, 5)
    print(f"10 / 5 = {result}")
    
    # Handling errors
    try:
        result = divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")
