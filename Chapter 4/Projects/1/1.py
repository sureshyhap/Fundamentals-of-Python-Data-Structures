import sys
sys.path.insert(0, "../../")
from arrays import Array

arr = Array(10, 5)
print(arr)

for item in arr:
    print(item)

arr.insert_end(20)
print(arr.size())
