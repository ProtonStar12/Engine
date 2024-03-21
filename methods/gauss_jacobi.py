import sympy as sp

def jacobi_method(matrix_input1, matrix_input2, x0, iteration):
    L = sp.Matrix([[matrix_input1[i, j] if i > j else 0 for j in range(matrix_input1.cols)] for i in range(matrix_input1.rows)])
    U = sp.Matrix([[matrix_input1[i, j] if i < j else 0 for j in range(matrix_input1.cols)] for i in range(matrix_input1.rows)])
    D = sp.diag(*matrix_input1.diagonal())
    
    LD_inv = (L + D).inv()
    
    B = matrix_input2
    
    X_prev = x0
    
    for i in range(iteration):
        X_next = LD_inv * (B - U * X_prev)
        print(f"Iteration {i+1} : ")
        sp.pprint(X_next)
        X_prev = X_next
        
    return X_next
    
def take_matrix_input(rows, cols):
    matrix = sp.zeros(rows, cols)
    
    print("Enter the matrix elements row by row : ")
    for i in range(rows):
        for j in range(cols):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            matrix[i, j] = element
            
    return matrix

