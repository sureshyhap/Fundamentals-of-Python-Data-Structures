from arrays import Array

class Grid(object):

    def __init__(self, rows, columns, fill_value=None):
        self.data = Array(rows, Array(columns, fill_value))

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __str__(self):
        s = ""
        for row in range(len(self.data)):
            s += str(self.data[row])
            if row != (len(self.data) - 1):
                s += '\n'
        return s

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, new_item):
        self.data[index] = new_item
