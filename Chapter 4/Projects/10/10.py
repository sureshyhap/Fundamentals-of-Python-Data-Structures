import sys
sys.path.insert(0, "../..")
from node import Node, pop

head = None
for i in range(10):
    head = Node(i, head)
(head, item) = pop(0, head)
    
temp = head

while temp.next:
    print(temp.data, end=" ")
    temp = temp.next
print(temp.data)
print(item)
