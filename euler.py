import sympy as sp


def euler_method(initial_y, h_value, end_point, f):
    # Define symbols
    x = sp.Symbol("x")
    y = sp.Symbol("y")

    # Define the differential equation dy/dx = f(x, y)

    parsed_eq = sp.sympify(f)

    # Initialize variables
    x_value = 0  # Start from x = 0
    y_value = initial_y

    # Perform Euler's method and print values at each point
    while x_value < end_point:
        # Print the current value of y
        print(f"At x = {x_value:.2f}, y = {y_value:.10f}")
        # Calculate the next y-value using Euler's method
        y_value += h_value * parsed_eq.subs({x: x_value, y: y_value})
        # Increment x
        x_value += h_value

    # Print the value of y at the end point
    print(f"At x = {end_point:.2f}, y = {y_value:.10f}")
