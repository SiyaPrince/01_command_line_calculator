# Command-Line Calculator

A beginner-friendly but progressively improved command-line calculator built with Python.

This project was created as the first practical project in a Python learning journey focused on writing code, solving problems, debugging independently, and gradually developing professional software-engineering habits.

## Project Overview

The application allows a user to perform basic arithmetic operations from the terminal:

- Addition
- Subtraction
- Multiplication
- Division

The calculator validates menu choices, handles invalid numeric input, prevents division by zero, and allows the user to perform multiple calculations during the same session.

## Purpose of the Project

The main purpose of this project was not only to build a calculator, but also to relearn Python fundamentals through practical coding.

The project developed progressively from a simple addition script into a structured command-line application containing reusable functions, input validation, control flow, and error handling.

## Features

- Interactive command-line interface
- Addition, subtraction, multiplication, and division
- Repeated calculations without restarting the application
- Validation of operation choices
- Validation of numeric input
- Protection against division by zero
- Clear result messages
- Functions for separating application responsibilities
- User-controlled continuation and exit flow

## Technologies Used

- Python 3
- Python standard library only

No external packages are required.

## Project Structure

```text
01_command_line_calculator/
├── calculator.py
└── README.md
```

## Requirements

Before running the application, ensure that Python 3 is installed.

Check the installed Python version with:

```bash
python --version
```

On Windows, this command may also be used:

```bash
py --version
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd 01_command_line_calculator
```

No additional dependencies need to be installed.

## Running the Application

Run the calculator with:

```bash
python calculator.py
```

On Windows, this may also work:

```bash
py calculator.py
```

## How to Use the Calculator

When the application starts, it displays the available arithmetic operations.

```text
1. Addition: +
2. Subtraction: -
3. Multiplication: *
4. Division: /
```

Enter the symbol for the required operation:

```text
+
-
*
/
```

The application then asks for two numbers.

Example:

```text
Enter the number corresponding to the operation (+, -, *, /): +
Enter a number: 12
Enter a number: 8

The result of 12.0 + 8.0 is: 20.0
```

After completing a calculation, the user can choose whether to continue or exit:

```text
1. Continue
2. Exit
```

## Example Session

```text
====================

Command Line Calculator!

====================

1. Addition: +
2. Subtraction: -
3. Multiplication: *
4. Division: /

Enter the number corresponding to the operation (+, -, *, /): *

Enter a number: 7
Enter a number: 6

The result of 7.0 * 6.0 is: 42.0

1. Continue
2. Exit

Do you want to perform another calculation? (1/2): 2
```

## Application Design

The application is divided into small functions. Each function is responsible for one main task.

### `display_menu()`

Displays the supported arithmetic operations.

### `get_operation()`

Collects the selected operation from the user and returns it to the main program.

### `get_numbers()`

Requests a number from the user.

The function uses a loop and exception handling to prevent invalid values from crashing the program.

```python
while True:
    try:
        number = float(input("Enter a number: "))
        return number
    except ValueError:
        print("Error: Please enter a valid number.")
```

### `calculate(first_number, second_number, operation_choice)`

Performs the selected arithmetic operation.

The function also checks whether the second number is zero before division.

### `continuation_menu()`

Asks whether the user wants to perform another calculation or exit.

It repeatedly requests input until the user enters a valid option.

## Program Flow

```text
Start application
        |
Display operation menu
        |
Get operation choice
        |
Validate operation
        |
Get first number
        |
Get second number
        |
Perform calculation
        |
Display result
        |
Continue or exit?
   |             |
Continue        Exit
   |             |
Return to menu  End application
```

## Python Concepts Practised

This project introduced and reinforced the following concepts:

- Variables
- Strings
- Floating-point numbers
- Arithmetic operators
- User input with `input()`
- Type conversion with `float()`
- Output with `print()`
- Conditional statements
- `if`, `elif`, and `else`
- `while` loops
- `break`
- `continue`
- Lists
- Membership checks using `in` and `not in`
- String methods
- Functions
- Function parameters
- Return values
- Exception handling
- `try` and `except`
- `ValueError`
- Input validation
- Division-by-zero validation
- f-strings
- Separation of responsibilities
- Basic refactoring

## Development Progression

The calculator was built incrementally.

### Version 1: Addition

The first version accepted two numbers and displayed their sum.

Concepts introduced:

- Variables
- `input()`
- `float()`
- `print()`
- Addition

### Version 2: Subtraction

Subtraction was added while improving variable naming with Python's `snake_case` convention.

### Version 3: Operation Menu

The user could choose between addition, subtraction, multiplication, and division.

Concepts introduced:

- Conditional statements
- Menu-driven programs
- Multiple arithmetic operators

### Version 4: Repeated Calculations

A `while` loop allowed the calculator to remain active until the user chose to stop.

Concepts introduced:

- Loops
- Changing program state
- Continuation logic

### Version 5: Validation and Edge Cases

The application began handling:

- Invalid operation choices
- Division by zero
- Application exit
- Continued calculations

Concepts introduced:

- `break`
- `continue`
- Membership validation
- Edge-case handling

### Version 6: Functions and Exception Handling

The program was refactored into reusable functions.

Invalid numeric input was handled using `try` and `except`.

Concepts introduced:

- Functions
- Parameters
- Return values
- Exception handling
- Separation of responsibilities

## Error Handling

### Invalid Number

If the user enters text instead of a number:

```text
Enter a number: hello
Error: Please enter a valid number.
```

The application asks for the number again instead of terminating.

### Division by Zero

If the user attempts to divide by zero:

```text
Error: Division by zero is not allowed.
```

### Invalid Operation

If the entered operation is unsupported:

```text
Invalid choice of operation. Please try again.
```

## Current Limitations

The current version has several areas that can still be improved:

- The displayed menu uses numbers, while the operation input expects arithmetic symbols.
- The application does not yet have automated tests.
- Calculation logic and result display are handled by the same function.
- The exit option is not displayed in the main operation menu.
- Results are displayed immediately instead of being returned for reuse.
- The application supports only four arithmetic operations.
- Calculation history is not stored.
- Very large or very small numbers are not specially formatted.

These limitations are documented intentionally because identifying weaknesses and planning improvements are important parts of software development.

## Recommended Improvements

Possible future improvements include:

1. Make the menu and operation input consistent.
2. Add an explicit exit option to the main menu.
3. Change `calculate()` so it returns the result instead of printing it.
4. Add a separate function for displaying results.
5. Add exponentiation, modulus, and floor division.
6. Store calculation history.
7. Allow users to view or clear history.
8. Add automated tests with `pytest`.
9. Add type hints.
10. Add docstrings to every function.
11. Place the main application flow inside a `main()` function.
12. Use:

```python
if __name__ == "__main__":
    main()
```

13. Split the project into multiple Python modules when it grows.
14. Package the application as an installable command-line tool.

## Future Development

This calculator is intended to evolve beyond a basic arithmetic application into a comprehensive mathematical calculator.

A future version of the project will introduce a wide range of advanced mathematical operations and scientific computing features while maintaining a modular and maintainable codebase.

### Planned Features

The planned enhancements include, but are not limited to:

- Exponentiation and roots
- Modulus and floor division
- Absolute value and rounding operations
- Logarithmic and exponential functions
- Trigonometric functions (sin, cos, tan)
- Inverse trigonometric functions
- Hyperbolic functions
- Factorials and combinations
- Permutations
- Prime number utilities
- Greatest Common Divisor (GCD)
- Least Common Multiple (LCM)
- Percentage calculations
- Statistical calculations (mean, median, mode, variance, standard deviation)
- Scientific notation support
- Memory functions (M+, M-, MR, MC)
- Calculation history
- Expression evaluation using operator precedence
- User-defined mathematical constants
- Unit conversions
- Number system conversions (Binary, Octal, Decimal, Hexadecimal)
- Matrix operations
- Complex number calculations
- Equation solving
- Polynomial operations
- Basic linear algebra utilities

### Long-Term Vision

The long-term objective is to transform this project into a fully featured command-line scientific calculator that demonstrates progressively advanced Python programming concepts and software engineering principles.

As the project evolves, additional concepts such as Object-Oriented Programming (OOP), modular architecture, automated testing, logging, configuration management, packaging, and documentation standards will be incorporated to ensure the application reflects professional software development practices.

This project will continue to serve as a learning platform, with each new version introducing more advanced Python features while maintaining clean, readable, and maintainable code.

## Lessons Learned

The most important lesson from this project is that software should be developed incrementally.

The calculator began as a small script and became more reliable through repeated improvements. Each version introduced only a few new concepts, allowing the existing knowledge to be reused while new skills were practised.

The project also demonstrated that working code is only the first stage. Good software should also be:

- Readable
- Structured
- Validated
- Maintainable
- Reusable
- Documented
- Easy to test
- Easy to improve

## Documentation Lessons

A useful project README should help another developer answer the following questions:

- What does the project do?
- Why was it created?
- What features does it contain?
- What technologies does it use?
- How is it installed?
- How is it run?
- How does the program work?
- How is the code organized?
- What was learned?
- What limitations remain?
- What could be improved next?

Documentation should be updated whenever the application's behaviour, setup, structure, or requirements change.

## Testing Checklist

The calculator can be manually tested with the following cases:

| Test | Input | Expected Behaviour |
|---|---|---|
| Addition | `10 + 5` | Displays `15` |
| Subtraction | `10 - 5` | Displays `5` |
| Multiplication | `10 * 5` | Displays `50` |
| Division | `10 / 5` | Displays `2` |
| Decimal input | `7.5 + 2.5` | Displays `10` |
| Negative input | `-4 + 10` | Displays `6` |
| Zero division | `10 / 0` | Displays an error |
| Invalid number | `abc` | Requests another number |
| Invalid operation | `%` | Displays an error |
| Continue | `1` | Returns to the operation menu |
| Exit | `2` | Ends the session |

## Portfolio Value

This project demonstrates more than arithmetic. It provides evidence of:

- Progressive problem solving
- Python fundamentals
- Input validation
- Error handling
- Refactoring
- Functional decomposition
- User-focused application flow
- Awareness of edge cases
- Technical documentation
- Ability to identify future improvements

## Author

**Siya**

Python Programmer and Systems Developer in training.

## License

This project is intended for learning and portfolio use.

A formal open-source licence can be added if the repository is made available for public reuse or contribution.
