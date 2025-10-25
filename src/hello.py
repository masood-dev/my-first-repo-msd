"""
hello.py - A simple Python script to demonstrate basic programming concepts

This is an example file for learning purposes.
"""


def greet(name):
    """
    Returns a greeting message for the given name.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to GitHub!"


def main():
    """
    Main function to demonstrate the greet function.
    """
    # Example usage
    message = greet("World")
    print(message)
    
    # You can also greet yourself
    your_name = "Developer"
    personal_greeting = greet(your_name)
    print(personal_greeting)


if __name__ == "__main__":
    main()
