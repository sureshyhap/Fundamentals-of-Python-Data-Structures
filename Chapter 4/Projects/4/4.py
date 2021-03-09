import sys
sys.path.insert(0, "../..")
from arrays import Array

arr = Array(10, 5)
arr.insert(3, 7)
print(arr)
arr.pop(3)
print(arr)
