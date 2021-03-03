import sys
sys.path.insert(0, "../../..")
from arrays import Array
from grid import Grid

class ThreeDMatrix(object):
    def __init__(self, depth, rows, columns, fill_value=None):
        self.data = Array(depth, Grid(rows, columns, fill_value))

    def __str__(self):
        s = ""
        for i in range(len(self.data)):
            s += str(self.data[i])
            s += '\n\n'
        return s

    def get_depth(self):
        return len(self.data)

    def get_height(self):
        return self.data[0].get_height()

    def get_width(self):
        return self.data[0].get_width()

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, new_item):
        self.data[index] = new_item
