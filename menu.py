# main_script.py
import os
import sympy as sp
from simple_term_menu import TerminalMenu
from methods.newton_rapshon_method import newton_raphson
from methods.composite_trapezoidal import integrate_equation
from methods.composite_simpson import integrate_simpson
from methods.romberg_one import rhomberg_trapezoidal
from methods.romberg_two import rhomberg_simpson
from methods.euler import euler_method
from methods.backward_euler import backward_euler_method
from methods.modified_euler import modified_euler_method
from methods.cauchy_euler import heuns_method
from methods.range_kutta import range_kutta_method
from methods.gauss_seidal import gauss_seidal_method, take_matrix_input
from methods.regula_falsi import regula_falsi_method


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


def rhomberg_option():
    menu_items = ["Trapezoidal", "Simpson", "Exit"]
    menu = TerminalMenu(menu_items)

    while True:
        selected_index = menu.show()
        if selected_index == 0:
            n_values = list(
                map(
                    float,
                    input("Enter the values of I separated by ',' : ")
                    .strip()
                    .split(","),
                )
            )
            rhomberg_trapezoidal(n_values)
        elif selected_index == 1:
            n_values = list(
                map(
                    float,
                    input("Enter the values of I separated by ',' : ")
                    .strip()
                    .split(","),
                )
            )
            rhomberg_simpson(n_values)
        elif selected_index == 2:
            break


def euler_menu():
    menu_items = [
        "First-Order",
        "Second-Order",
        "Third-Order",
        "Fourth-Order",
        "Backward",
        "Modified",
        "Cauchy",
        "Back",
    ]
    menu = TerminalMenu(menu_items)

    while True:
        selected_index = menu.show()
        if selected_index == 0:
            f = input("Enter the equation : ")
            initial_y = float(input("Enter the initial value of y (y0): "))
            h_value = float(input("Enter the value of h: "))
            end_point = float(input("Enter the end point (x-value): "))
            euler_method(initial_y, h_value, end_point, f)
        elif selected_index == 1:
            print("under work")
        elif selected_index == 2:
            print("under work")
        elif selected_index == 3:
            print("under work")
        elif selected_index == 4:
            initial_y = float(input("Enter the value of y(0) : "))
            h_value = float(input("Enter the value of h : "))
            end_point = float(input("Enter the end point : "))
            f = input("Enter the equation : ")
            backward_euler_method(initial_y, h_value, end_point, f)
        elif selected_index == 5:
            initial_y = float(input("Enter the value of y(0) : "))
            h_value = float(input("Enter the value of h : "))
            end_point = float(input("Enter the end point : "))
            f = input("Enter the equation : ")
            modified_euler_method(initial_y, h_value, end_point, f)
        elif selected_index == 6:
            initial_y = float(input("Enter the value of y(0) : "))
            h_value = float(input("Enter the value of h : "))
            end_point = float(input("Enter the end point : "))
            f = input("Enter the equation : ")
            heuns_method(initial_y, h_value, end_point, f)
        elif selected_index == 7:
            break


def taylor_menu():
    menu_items = ["Euler", "Range-Kutta", "Back"]
    menu = TerminalMenu(menu_items)

    while True:
        selected_index = menu.show()
        if selected_index == 0:
            euler_menu()
        elif selected_index == 1:
            f = input("Enter the equation y' = ")
            initial_y = float(input("Enter the value of y(0) : "))
            h_value = float(input("Enter the value of h : "))
            end_point = float(input("Enter the value of end 'x-point' : "))
            decimal_points = int(
                input("Enter the value of decimals you want : "))
            range_kutta_method(initial_y, h_value,
                               end_point, f, decimal_points)
        elif selected_index == 2:
            break


def matrix():
    menu_items = ["Seidal", "Jacobi", "Power", "Back"]
    menu = TerminalMenu(menu_items)

    while True:
        selected_index = menu.show()
        if selected_index == 0:
            decimals = int(input("Enter the number of decimals: "))
            rows_A = int(input("Enter the number of rows for matrix A: "))
            cols_A = int(input("Enter the number of columns for matrix A: "))
            matrix_input_A = take_matrix_input(rows_A, cols_A, decimals)
            rows_B = int(input("Enter the number of rows for matrix B: "))
            cols_B = int(input("Enter the number of columns for matrix B: "))
            matrix_input_B = take_matrix_input(rows_B, cols_B, decimals)
            matrix_input_X0 = take_matrix_input(rows_B, cols_B, decimals)
            iterations = int(input("Enter the number of iterations : "))
            result = gauss_seidal_method(
                matrix_input_A, matrix_input_B, matrix_input_X0, iterations, decimals)
            print("Final Result (X_final):")
            sp.pprint(result)
        elif selected_index == 1:
            print("under work")
        elif selected_index == 2:
            print("under work")
        elif selected_index == 3:
            break


def interation():
    menu_items = ["Composite-Trapezoidal",
                  "Composite-Simpson", "Rhomberg", "Back"]
    menu = TerminalMenu(menu_items)

    while True:
        selected_index = menu.show()
        if selected_index == 0:
            a = float(input("enter the value of a : "))
            b = float(input("enter the value of b : "))
            equation = input("enter the equation : ")
            n_values_str = input(
                "Enter the list of values for n separated by ',' : "
            )
            n_values = [int(value) for value in n_values_str.split(",")]
            integrate_equation(
                a, b, equation, n_values
            )  # Call your function for integrating equations
        elif selected_index == 1:
            a = float(input("enter value of a : "))
            b = float(input("enter value of b : "))
            equation = input("enter the equation : ")
            n_values = list(
                map(
                    int,
                    input("enter the values of N separated by ',' : ")
                    .strip()
                    .split(","),
                )
            )
            integrate_simpson(a, b, equation, n_values)
        elif selected_index == 2:
            rhomberg_option()
        elif selected_index == 3:
            break


def clear_menu():
    os.system("cls" if os.name == "nt" else "clear")


def header(filename):
    with open(filename, "r") as f:
        ascii_art = f.read()
        print(ascii_art)


def main():

    header("Engine.txt")

    menu_items = [
        "Add",
        "Subtract",
        "Multiply",
        "Divide",
        "Regula-Falsi",
        "Newton-Raphson",
        "Integration-Methods",
        "Diff-Equation",
        "Matrix-Methods",
        "Exit",
    ]
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
            equation_str = input("Enter the equation: ")
            iterations = int(input("Enter the number of iterations: "))
            decimals = int(
                input("Enter the number of decimal points to display: "))
            regula_falsi_method(equation_str, iterations, decimals)
        elif selected_index == 5:
            equation_str = input("Enter the equation (in terms of 'x'): ")
            x0 = float(input("Enter initial guess: "))
            iterations = int(input("Enter number of iterations: "))
            newton_raphson(equation_str, x0, iterations)
        elif selected_index == 6:
            interation()

        elif selected_index == 7:
            taylor_menu()
        elif selected_index == 8:
            matrix()
        elif selected_index == 9:
            break
    clear_menu()


if __name__ == "__main__":
    main()
