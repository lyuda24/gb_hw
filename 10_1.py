from copy import deepcopy


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) > len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


m1 = Matrix([[1, 2, 3], [1, 4, 0]])
m2 = Matrix([[3, 2, 1], [4, 1, 0]])
print(m1)
print(" ")
print(m2)
print(" ")
print(m1 + m2)
