# main_script.py

from simple_term_menu import TerminalMenu
from newton_rapshon_method import newton_raphson


def add_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("The result of addition is:", result)


def subtract_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("The result of subtraction is:", result)


def multiply_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("The result of multiplication is:", result)


def divide_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2
        print("The result of division is:", result)


def main():
    menu_items = ["Add", "Subtract", "Multiply", "Divide", "Newton-Raphson", "Exit"]
    menu = TerminalMenu(menu_items)

    while True:
        selected_index = menu.show()
        if selected_index == 0:
            add_numbers()
        elif selected_index == 1:
            subtract_numbers()
        elif selected_index == 2:
            multiply_numbers()
        elif selected_index == 3:
            divide_numbers()
        elif selected_index == 4:
            equation_str = input("Enter the equation (in terms of 'x'): ")
            x0 = float(input("Enter initial guess: "))
            iterations = int(input("Enter number of iterations: "))
            newton_raphson(equation_str, x0, iterations)
        elif selected_index == 5:
            break


if __name__ == "__main__":
    main()

