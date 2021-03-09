import sys
sys.path.insert(0, "../..")
from arrays import Array

arr = Array(10)
arr.insert_end(20)
arr.shrink()
print(arr)
