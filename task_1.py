# We use the matrix of integers!!!
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.m, self.n, self._is_valid = self.__check_dimensions()
        if not self._is_valid:
            raise ValueError('Invalid matrix!')

    def __check_dimensions(self):
        if len(set([len(x) for x in self.matrix])) > 1 or not all(isinstance(y, int) for x in self.matrix for y in x):
            return 0, 0, False
        else:
            m = len(self.matrix)
            n = len(self.matrix[0])
            return m, n, True

    def __add__(self, other):
        if (self.m, self.n) != (other.m, other.n):
            return "Dimension error! Matrices must be of the same dimensions."
        else:
            return Matrix([list(map(lambda a, b: a + b, x, y)) for x, y in zip(self.matrix, other.matrix)])

    def __str__(self):
        return '\n'.join(['\t'.join([str(x) for x in y]) for y in self.matrix])

    def __eq__(self, other):
        return all(x[0] == x[1] for x in zip(self.matrix, other.matrix))

    def matrix_transpose(self):
        return Matrix([list(i) for i in zip(*self.matrix)])


# Incorrect matrix
mat01 = [[[1, 2], 0, 0, 8],
         [0, 2, 0, 9],
         [0, 0, 0, 10]]

mat02 = [[1, 0, 0, 8],
         [0, 2, 0, 9, 7],
         [0, 0, 0, 10]]

# Simple matrix
mat1 = [[1, 0, 0, 8],
        [0, 2, 0, 9],
        [0, 0, 0, 10]]
mat2 = [[9, 0, 0, 8],
        [0, 66, 0, 9],
        [0, 0, 9, 10]]

# Column vector
mat3 = [[1], [2], [3]]
mat4 = [[4], [5], [6]]

# Row vector
mat5 = [[1, 2, 3]]
mat6 = [[4, 5, 6]]

try:
    matrix0 = Matrix(mat01)
except ValueError:
    print(f"Incorrect matrix")
try:
    matrix0 = Matrix(mat02)
except ValueError:
    print(f"Incorrect matrix")


matrix1 = Matrix(mat1)
matrix2 = Matrix(mat2)
matrix3 = Matrix(mat3)
matrix4 = Matrix(mat4)
matrix5 = Matrix(mat5)
matrix6 = Matrix(mat6)
print(f"matrix1 + matrix2 = \n{matrix1 + matrix2}")
print(f"matrix1 is equal to matrix1 ? {matrix1 == matrix1}")
print(f"matrix1 is equal to matrix2 ? {matrix1 == matrix2}")
print(f"matrix3 + matrix4 = \n{matrix3 + matrix4}")
print(f"matrix5 + matrix6 = {matrix5 + matrix6}")
print(f"matrix3 transposed = \n{matrix3.matrix_transpose()}")
