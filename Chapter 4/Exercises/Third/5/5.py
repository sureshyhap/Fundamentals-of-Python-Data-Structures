import sys
sys.path.insert(0, "../../..")
from arrays import Array

class Ragged_Grid():

    def __init__(self, rows, columns_list, fill_value=None):
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns_list[row], fill_value)

    def __str__(self):
        s = ""
        for row in range(len(self.data)):
            s += str(self.data[row])
            if row != len(self.data) - 1:
                s += '\n'
        return s

if __name__ == "__main__":
    rg = Ragged_Grid(3, [2, 5, 3], 0)
    print(rg)
            
        
