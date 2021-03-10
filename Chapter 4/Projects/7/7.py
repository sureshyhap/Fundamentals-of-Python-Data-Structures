import sys
sys.path.insert(0, "../..")
from grid import Grid
from arrays import Array

class Matrix(Grid):

    def __init__(self, rows, columns, fill_value=None):
        super(Matrix, self).__init__(rows, columns, fill_value)

    def __add__(self, other):
        if self.data.size() != other.data.size() or self.data[0].size() != other.data[0].size():
            return
        sum = Matrix(self.data.size(), self.data[0].size())
        for i in range(self.data.size()):
            sum[i] = (self.data[i] + other.data[i])
        return sum

    def __sub__(self, other):
        if self.data.size() != other.data.size() or self.data[0].size() != other.data[0].size():
            return
        sum = Matrix(self.data.size(), self.data[0].size())
        for i in range(self.data.size()):
            sum[i] = (self.data[i] - other.data[i])
        return sum

    def __mul__(self, other):
        """ Matrix multiplication not element-wise multiplication """
        if self.get_width() != other.get_height():
            return
        result = Matrix(self.get_height(), other.get_width(), 0)
        for i in range(self.get_height()):
            row_result = Array(other.get_width(), 0)
            for j in range(other.get_width()):
                second = Array(other.get_height(), 0)
                for k in range(second.size()):
                    second[k] = other[k][j]
                scalar_result = self.data[i] * second
                row_result[j] = scalar_result
            result[i] = row_result
        return result
        
"""
m1 = Matrix(3, 4, 10)
m2 = Matrix(3, 4, 11)
print(m1 - m2)
"""

m = Matrix(2, 3, 0)
n = Matrix(3, 4, 0)

first_row1 = Array(3, 0)
first_row1[0] = 1
first_row1[1] = 2
first_row1[2] = 3
m[0] = first_row1
first_row2 = Array(3, 0)
first_row2[0] = 4
first_row2[1] = 5
first_row2[2] = 6
m[1] = first_row2

print(m)
print()

second_row1 = Array(4, 0)
second_row1[0] = 7
second_row1[1] = 1
second_row1[2] = 4
second_row1[3] = 7
n[0] = second_row1
second_row2 = Array(4, 0)
second_row2[0] = 8
second_row2[1] = 2
second_row2[2] = 5
second_row2[3] = 8
n[1] = second_row2
second_row3 = Array(4, 0)
second_row3[0] = 9
second_row3[1] = 3
second_row3[2] = 6
second_row3[3] = 9
n[2] = second_row3

print(n)
print()

print(m * n)


