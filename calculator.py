# Display calculator name

from ast import While


print("=" * 20)
print()
print("Command Line Calculator!")
print()
print("=" * 20)
print()

# Display menu of operations

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

print()
# Take operation input from the user

operation_choice = input("Enter the number corresponding to the operation (1/2/3/4): ")

print()
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
    print(f"The quotient of {first_number} and {second_number} is: {first_number / second_number}")
else:
    print("Invalid choice of operation.")
