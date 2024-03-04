import sympy as sp
from sympy import symbols, lambdify, diff


def newton_raphson(equation_str, x0, iterations):
    x = symbols("x")
    equation = sp.sympify(equation_str)
    f = lambdify(x, equation)
    f_prime = lambdify(x, diff(equation, x))

    x_val = x0
    for i in range(iterations):
        x_val = x_val - f(x_val) / f_prime(x_val)
        print(f"Iteration {i + 1}: Approximate root: {x_val}")

    print("Final Approximate root:", x_val)
