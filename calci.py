# Basic Calculator Program
# Functions for arithmetic operations

# Function to perform addition 
def addition(a, b):
    return a + b

# Function to perform subtraction 
def subtraction(a, b):
    return a - b

# Function to perform multiplication
def multiplication(a, b):
    return a * b

# Function to perform division 
def division(a, b):
    return a / b if b != 0 else "Error: Division by zero"

# Display menu options
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take user input
choice = input("Input your choice(1/2/3/4): ")

# Validate choice
if choice in ('1', '2', '3', '4'):
    num_one = float(input("Enter first number: "))
    num_two = float(input("Enter second number: "))

    # Perform operation based on choice
    if choice == '1':
        print("Result:", addition(num_one, num_two))
    elif choice == '2':
        print("Result:", subtraction(num_one, num_two))
    elif choice == '3':
        print("Result:", multiplication(num_one, num_two))
    elif choice == '4':
        print("Result:", division(num_one, num_two))
else:
    print("Invalid choice! Please select a valid operation.")
