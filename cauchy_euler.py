import sympy as sp

def heuns_method(initial_y,h_value,end_point,f):
 
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
        K2 = h_value * parsed_eq.subs({x: x_value + h_value, y: y_value + K1})
        # Calculate the next y-value using Heun's method
        y_next = y_value + (K1 + K2) / 2
        # Print the values
        print(f"Iteration {iteration}: y{iteration} = {y_value:.10f}, K1 = {K1:.10f}, K2 = {K2:.10f}")
        # Update y_value for the next iteration
        y_value = y_next
        # Increment the iteration number
        iteration += 1
        # Update x_value for the next iteration
        x_value += h_value
    
    # Print the final value of y
    print(f"Iteration {iteration}: y{iteration} = {y_value:.10f}")

