import sympy as sp
import numpy as np


def regula_falsi_method(func, a, b, tol=1e-6, max_iter=100, decimals=6):
    """
    Regular Falsi method to find root of a function.

    Parameters:
    func (function): The target function.
    a (float): The left endpoint of the initial interval.
    b (float): The right endpoint of the initial interval.
    tol (float): The tolerance for the stopping criteria.
    max_iter (int): Maximum number of iterations.
    decimals (int): Number of decimal points to display.

    Returns:
    float: Approximation of the root.
    """
    # Check if the signs of the function at the endpoints are opposite
    if func(a) * func(b) >= 0:
        raise ValueError(
            "The function values at the endpoints must have opposite signs.")

    # Initialize iteration counter and initial interval
    iteration = 0
    interval_width = abs(b - a)

    while interval_width > tol and iteration < max_iter:
        # Calculate the intersection point with x-axis using false position formula
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        # Update the interval
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        # Print the value of x at each iteration with the specified number of decimals
        print(f"Iteration {iteration + 1}: x = {c:.{decimals}f}")

        # Update interval width and iteration counter
        interval_width = abs(b - a)
        iteration += 1

    return (a + b) / 2


def regular_falsi_solver(equation_str, iterations, decimals):
    # Convert the equation string to a SymPy equation
    x = sp.symbols('x')
    equation = sp.sympify(equation_str)

    # Convert the SymPy equation to a callable Python function
    f = sp.lambdify(x, equation)

    # Find the initial interval [a, b] with sign changes in the function among integers in the range from 0 to 100
    initial_points = []
    for i in range(101):
        if i == 100:
            break
        if f(i) * f(i + 1) < 0:
            initial_points.append((i, i + 1))

    if not initial_points:
        raise ValueError(
            "No initial interval found among integers in the range from 0 to 100. Consider choosing a different equation or expanding the search range.")

    print("Initial intervals with sign changes in the function:")
    for i, (a, b) in enumerate(initial_points):
        print(f"Interval : [{a}, {b}]")

    # Select the first initial interval found
    a, b = initial_points[0]

    # Find the root using Regular Falsi method
    regula_falsi_method(f, a, b, max_iter=iterations, decimals=decimals)
