import sys
sys.path.insert(0, "../..")
from grid import Grid

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

m1 = Matrix(3, 4, 10)
m2 = Matrix(3, 4, 11)
print(m1 + m2)
            
