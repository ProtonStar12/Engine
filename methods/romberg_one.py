def rhomberg_trapezoidal(n_values):
    def perform_operation(values, iteration_number):
        results = []
        for i in range(1, len(values)):
            result = ((4.0**(iteration_number-1)) * values[i] - values[i-1]) / ((4.0**(iteration_number-1) - 1))
            results.append(result)
        return results

    for iteration_number in range(2, len(n_values) + 1):
        # Perform the operation
        n_values = perform_operation(n_values, iteration_number)
        
        # Print the values obtained in this iteration
        print(f"Iteration {iteration_number-1} values: {n_values}")

    return n_values[0]





