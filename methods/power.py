import sympy as sp


def take_matrix_input(rows, cols):
    matrix = sp.zeros(rows, cols)

    print("Enter the matrix elements row by row:")
    for i in range(rows):
        for j in range(cols):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            matrix[i, j] = element

    return matrix


def calculate_eigenvalues(matrix_input1, X0, decimals):

    # Set initial difference arbitrarily large to start the loop
    difference = float('inf')

    # Initialize X_prev with X0
    X_prev = X0

    # Initialize iteration counter
    iteration = 0

    # Iterate until difference falls below the specified decimals
    while difference >= 1 / 10**decimals:
        # Perform the iteration
        Y = matrix_input1 * X_prev
        m = max(Y)

        # Normalize the vector
        max_value = max(Y)
        X_new = Y / max_value

        # Calculate difference between consecutive iterations
        difference = max(abs(X_new - X_prev))

        # Print values at each iteration
        print(f"Iteration {iteration+1}:")
        print("X:", X_new)
        print("Y:", Y)
        print("m:", m)
        print("Difference:", difference)
        print()

        # Update X_prev for next iteration
        X_prev = X_new

        # Increment iteration counter
        iteration += 1

    # Calculate eigenvalues
    eigenvalue = sp.Matrix(
        Y.shape[0], Y.shape[1], lambda i, j: Y[i, j] / X_prev[i, j])

    print("Eigenvalues:", eigenvalue)

