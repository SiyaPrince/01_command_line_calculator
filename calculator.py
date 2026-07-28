# Display calculator name

print("=" * 20)
print()
print("Command Line Calculator!")
print()
print("=" * 20)
print()

# Functions

# Function that displays the operations menu.

def display_menu():
        
    print("1. Addition: +")
    print("2. Subtraction: -")
    print("3. Multiplication: *")
    print("4. Division: /")

    print()

# Function to get operation

def get_operation():
    operation_choice = input("Enter the number corresponding to the operation (+, -, *, /): ")
    return operation_choice

# Function to get numbers from the user

def get_numbers():
    while True:
        try:
            number = float(input("Enter a number: "))
            return number
        except ValueError:
            print("Error: Please enter a valid number.")

# Function to perform the calculation based on the operation choice

def calculate(first_number, second_number, operation_choice):

    operation, result = "", 0

    if operation_choice == "+":
        result = first_number + second_number
        operation = "sum"
    elif operation_choice == "-":
        result = first_number - second_number
        operation = "difference"
    elif operation_choice == "*":
        result = first_number * second_number
        operation = "product"
    elif operation_choice == "/":
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = first_number / second_number
            operation = "quotient"

    return result, operation

# Display the result of the calculation
def display_result(result, operation):
    if operation:
        print(f"The {operation} of {first_number} and {second_number} is: {result}")
    else:
        print("No valid operation was performed.")
# Continuation menu function

def continuation_menu():

    print("1. Continue")
    print("2. Exit")
    print()
    
    while True:
        choice = input("Do you want to perform another calculation? (1/2): ")
        if choice in ["1", "2"]:
            return choice
        else:
            print("Invalid input. Please enter '1' or '2'.")

# Initialize loop control variable

continue_choice = "Continue"

while continue_choice.lower() == "continue":

    # Display menu of operations

    display_menu()

    # Take operation input from the user

    operation_choice = get_operation()

    print()

    if operation_choice not in ["+", "-", "*", "/"]:
        if operation_choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        print("Invalid choice of operation. Please try again.")
        print()
        continue

    # Take in inputs of the numbers

    first_number = get_numbers()
    second_number = get_numbers()

    print()

    # Perform the selected operation calculation and display the result

    result = calculate(first_number, second_number, operation_choice)[0]
    operation = calculate(first_number, second_number, operation_choice)[1]

    # Display the result of the calculation

    display_result(result, operation)

    print()
    
    # Ask whether use wants to continue or not

    continue_choice = continuation_menu()

    if continue_choice == "1":
        continue_choice = "Continue"
    elif continue_choice == "2":
        continue_choice = "Exit"

    print()