import sympy as sp


def range_kutta_method(initial_y, h_value, end_point, f, decimal_points):

    x = sp.Symbol('x')
    y = sp.Symbol('y')

    parsed_eq = sp.sympify(f)

    x_value = 0
    y_value = initial_y
    iteration = 0

    while x_value < end_point:
        # Calculate K1
        K1 = h_value * parsed_eq.subs({x: x_value, y: y_value})
        # Calculate K2
        K2 = h_value * \
            parsed_eq.subs({x: x_value + h_value/2, y: y_value + K1/2})
        # Calculate K3
        K3 = h_value * \
            parsed_eq.subs({x: x_value + h_value/2, y: y_value + K2/2})
        # Calculate K4
        K4 = h_value * parsed_eq.subs({x: x_value + h_value, y: y_value + K3})
        # Calculate the next y-value using Runge-Kutta method equation
        y_next = y_value + (K1 + 2*K2 + 2*K3 + K4) / 6
        # Print the values
        print(f"Iteration {iteration}: y({x_value}) = {y_value}, K1 = {round(K1, decimal_points)}, K2 = {
              round(K2, decimal_points)}, K3 = {round(K3, decimal_points)}, K4 = {round(K4, decimal_points)}")
        # Update y_value for the next iteration
        y_value = round(y_next, decimal_points)
        # Increment the iteration number
        iteration += 1
        # Update x_value for the next iteration
        x_value += h_value

    # Print the final value of y
    print(f"Iteration {iteration}: y({x_value}) = {
          round(y_value, decimal_points)}")
