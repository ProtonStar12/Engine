import sympy as sp

# Function to take matrix input


def take_matrix_input_seidal(rows, cols, decimals):
    # Initializing an empty matrix
    matrix = sp.zeros(rows, cols)

    # Taking matrix elements input
    print("Enter the matrix elements row by row:")
    for i in range(rows):
        for j in range(cols):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            matrix[i, j] = round(element, decimals)

    return matrix

# Jacobi Iterative Method


def gauss_seidal_method(matrix_input_A, matrix_input_B, matrix_input_X0, iterations, decimals):
    # Function for Seidal iteration
    def seidal_iteration(A, B, X0, iterations, decimals):
        n = A.rows
        D = A.extract(range(n), range(n))
        L_U = A - D
        X = X0
        for i in range(iterations):
            X = D.inv() * (B - L_U * X)
            print(f"Iteration {i+1}:")
            # Format each element in the matrix to the specified number of decimals
            formatted_X = sp.Matrix(
                [[format(element.evalf(), f'.{decimals}f') for element in row] for row in X.tolist()])
            sp.pprint(formatted_X)
        return X

    # Perform Seidal Iteration
    result = seidal_iteration(
        matrix_input_A, matrix_input_B, matrix_input_X0, iterations, decimals)

    # Return the result
    return result

