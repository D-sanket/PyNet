import sys
from random import random, uniform


class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.array = []

        for i in range(rows):
            t = []
            for j in range(cols):
                t.append(0)
            self.array.append(t)

    def plus(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            print("Cannot add "+str((self.rows, self.cols))+" matrix with "+str((matrix.rows, matrix.cols)))
            return
        m = Matrix(self.rows, self.cols)
        m.array = []

        for i in range(self.rows):
            t = []
            for j in range(self.cols):
                t.append(self.array[i][j] + matrix.array[i][j])
            m.array.append(t)
        return m

    def minus(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            print("Cannot subtract "+str((matrix.rows, matrix.cols))+" matrix from "+str((self.rows, self.cols)))
            return
        m = Matrix(self.rows, self.cols)
        m.array = []

        for i in range(self.rows):
            t = []
            for j in range(self.cols):
                t.append(self.array[i][j] - matrix.array[i][j])
            m.array.append(t)
        return m

    def times(self, n):
        m = Matrix(self.rows, self.cols)
        m.array = []

        for i in range(self.rows):
            t = []
            for j in range(self.cols):
                t.append(self.array[i][j]*n)
            m.array.append(t)
        return m

    def hadamardProduct(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            print("Cannot perform hadamard product on "+str((matrix.rows, matrix.cols))+" and "+str((self.rows, self.cols)))
        m = Matrix(self.rows, self.cols)
        m.array = []

        for i in range(self.rows):
            t = []
            for j in range(self.cols):
                t.append(self.array[i][j] * matrix.array[i][j])
            m.array.append(t)
        return m

    def multiply(self, matrix):
        if self.cols != matrix.rows:
            print("Cannot multiply "+str((matrix.rows, matrix.cols))+" and "+str((self.rows, self.cols)))
            sys.exit(0)
        m = Matrix(self.rows, matrix.cols)
        for i in range(self.rows):
            for j in range(matrix.cols):
                m.array[i][j] = 0
                for k in range(matrix.rows):
                    m.array[i][j] += self.array[i][k] * matrix.array[k][j]
        return m

    def transpose(self):
        m = Matrix(self.cols, self.rows)

        for i in range(self.rows):
            for j in range(self.cols):
                m.array[j][i] = self.array[i][j]
        return m

    def flatten(self):
        m = []
        for row in self.array:
            m += row
        return m

    def forEach(self, func):
        m = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                m.array[i][j] = func(self.array[i][j])

        return m

    def reshape(self, dim):
        m = Matrix(dim[0], dim[1])
        f = self.flatten()
        k = 0

        for i in range(dim[0]):
            for j in range(dim[1]):
                m.array[i][j] = f[k]
                k += 1
        return m

    def toArray(self):
        m = []
        for i in range(self.rows):
            t = []
            for j in range(self.cols):
                t.append(float("%.2f" % self.array[i][j]))
            m.append(t)
        return m

    def load(self, array):
        m = Matrix.fromArray([array])
        m = m.reshape((self.rows, self.cols))
        return m

    def randomize(self):
        return self.forEach(self._random)

    def _random(self, x):
        return uniform(-1, 1)

    @staticmethod
    def fromArray(arr):
        m = Matrix(len(arr), len(arr[0]))
        m.array = arr
        return m

    @staticmethod
    def withDim(dim):
        return Matrix(dim[0], dim[1])
