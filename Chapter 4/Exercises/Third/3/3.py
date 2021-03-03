import sys
sys.path.insert(0, "../../../")
import arrays, grid

rows = 2
columns = 3

g = grid.Grid(rows, columns, 0)
g[0][1] = -5
g[1][2] = -10

def find_neg(g):
    h = g.get_height()
    w = g.get_width()
    for i in range(h):
        for j in range(w):
            if g[i][j] < 0:
                return g[i][j], i, j
    return 0, h, w

neg_num, row, column = find_neg(g)
print(neg_num, row, column)
