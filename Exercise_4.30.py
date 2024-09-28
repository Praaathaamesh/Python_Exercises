# Function to multiply two matrices
def multiply_matrices(matA, matB):
    # Get the dimensions
    rows_a = len(matA)
    cols_a = len(matA[0])
    rows_b = len(matB)
    cols_b = len(matB[0])
    # Check if multiplication is possible
    if cols_a != rows_b:
        print("Matrices cannot be multiplied. Number of columns in A must be equal to the number of rows in B.")
        return None
    # Initialize the result matrix with zeroes
    resultmat = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    # Perform multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                resultmat[i][j] += matA[i][k] * matB[k][j]
    
    return resultmat
# Example
matA = [[1, 2],[3, 4]]
matB = [[5, 6],[7, 8]]
result = multiply_matrices(matA, matB)
for row in result:
    print(row)