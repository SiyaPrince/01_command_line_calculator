# Display calculator name

print("=" * 20)
print()
print("Command Line Calculator!")
print()
print("=" * 20)
print()

# Initialize loop control variable

continue_choice = "Yes"

while continue_choice.lower() == "yes":

    # Display menu of operations

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    print()

    # Take operation input from the user

    operation_choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

    print()
    
    if operation_choice == "5":
        print("Exiting the calculator. Goodbye!")
        break

    if operation_choice not in ["1", "2", "3", "4"]:
        print("Invalid choice of operation. Please try again.")
        print()
        continue

    # Take in inputs of the numbers

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    print()

    # Perform the selected operation and display the result

    if operation_choice == "1":
        print(f"The sum of {first_number} and {second_number} is: {first_number + second_number}")
    elif operation_choice == "2":
        print(f"The difference between {first_number} and {second_number} is: {first_number - second_number}")
    elif operation_choice == "3":
        print(f"The product of {first_number} and {second_number} is: {first_number * second_number}")
    elif operation_choice == "4":
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
            print()
            continue
        else:
            print(f"The quotient of {first_number} and {second_number} is: {first_number / second_number}")
    else:
        print("Invalid choice of operation.")

    print()

    # Ask whether use wants to continue or not

    continue_choice = input("Do you want to perform another calculation? (Yes/No): ")

    print()