import sys
sys.path.insert(0, "../../..")
from arrays import Array

class Node(object):

    def __init__(self, data, next):
        self.data = data
        self.next = next

a = Array(10)
for i in range(10):
    a[i] = i

node = None
for i in range(len(a) - 1, -1, -1):
    node = Node(a[i], node)

while node != None:
    print(node.data, end=" ")
    node = node.next
print()
    
