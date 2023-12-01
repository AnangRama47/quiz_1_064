class MatrixOperations:
    def _init_(self, matrix):
        self.matrix = matrix

    def find_min_max(self):
        min_value = min(min(row) for row in self.matrix)
        max_value = max(max(row) for row in self.matrix)
        return min_value, max_value

    def transpose(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return transposed_matrix

    def matrix_multiplication(self, other_matrix):
        if len(self.matrix[0]) != len(other_matrix):
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        
        result_matrix = [[sum(a * b for a, b in zip(row, col)) for col in zip(*other_matrix)] for row in self.matrix]
        return result_matrix

    def matrix_addition(self, other_matrix):
        if len(self.matrix) != len(other_matrix) or len(self.matrix[0]) != len(other_matrix[0]):
            raise ValueError("The matrices must have the same dimensions for addition.")
        
        result_matrix = [[self.matrix[i][j] + other_matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return result_matrix


if __name__ == "_main_":
    matrix_a = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    matrix_operations = MatrixOperations(matrix_a)

    # Menghitung element terbesar dan terkecil
    min_value, max_value = matrix_operations.find_min_max()
    print(f"Elemen terkecil: {min_value}")
    print(f"Elemen terbesar: {max_value}")

    # Transpose matrix
    transposed_matrix = matrix_operations.transpose()
    print("Transposed matrix:")
    for row in transposed_matrix:
        print(row)

    # Menghitung perkalian dengan transpose
    matrix_b = matrix_operations.transpose()
    multiplication_result = matrix_operations.matrix_multiplication(matrix_b)
    print("Hasil perkalian matrix A dan transpose:")
    for row in multiplication_result:
        print(row)

    # Menghitung penjumlahan matrix dengan transpose
    addition_result = matrix_operations.matrix_addition(matrix_b)
    print("Hasil penjumlahan matrix A dan transpose:")
    for row in addition_result:
        print(row)
