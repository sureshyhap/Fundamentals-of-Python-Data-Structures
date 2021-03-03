import sys
sys.path.insert(0, "../../..")
from arrays import Array
from grid import Grid
from three_d_matrix import ThreeDMatrix

if __name__ == "__main__":
    threedm = ThreeDMatrix(2, 3, 4)
    depth = threedm.get_depth()
    height = threedm.get_height()
    width = threedm.get_width()
    for d in range(depth):
        gr = Grid(height, width)
        for h in range(height):
            ar = Array(width)
            for w in range(width):
                #((threedm[d])[h])[w] = (str(d) + str(h) + str(w))
                #threedm.__getitem__(d).__getitem__(h).__setitem__(w, (str(d) + str(h) + str(w)))
                ar.__setitem__(w, (str(d) + str(h) + str(w)))
            gr.__setitem__(h, ar)
        threedm.__setitem__(d, gr)            
    print(threedm)
                

