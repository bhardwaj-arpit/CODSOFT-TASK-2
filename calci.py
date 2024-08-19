import time
import os


# Fancy banner for the calculator
def display_banner():
    print("╔═══════════════════════════════════════════╗")
    print("║                                           ║")
    print("║           *** PYTHON CALCULATOR ***       ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")
    print("\n")


# Animating text for dramatic effect
def animate_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print("\n")


# A little delay for the fun of it
def dramatic_pause(seconds=1):
    time.sleep(seconds)


# Getting user input with a twist
def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            animate_text("Oops! That's not a valid number. Please try again.")


# Perform the calculation
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Invalid operation"


# Main calculator function
def calculator():
    display_banner()
    dramatic_pause(1)

    animate_text("Hello! Welcome to the Python Calculator.", 0.07)
    dramatic_pause(1)

    num1 = get_number_input("Enter the first number: ")
    dramatic_pause(0.5)

    num2 = get_number_input("Enter the second number: ")
    dramatic_pause(0.5)

    animate_text("Choose an operation: +, -, *, /", 0.05)
    operation = input("Enter your choice: ")

    dramatic_pause(0.5)
    animate_text("Calculating the result...", 0.07)
    dramatic_pause(2)

    result = calculate(num1, num2, operation)
    animate_text(f"The result of {num1} {operation} {num2} is: {result}", 0.05)

    dramatic_pause(1)
    animate_text("Thank you for using the Python Calculator!", 0.07)
    dramatic_pause(1)
    animate_text("Goodbye!", 0.1)


if __name__ == "__main__":
    calculator()
