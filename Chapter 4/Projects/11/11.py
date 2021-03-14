import sys
sys.path.insert(0, "../..")
from node import Node, TwoWayNode, length, insert, pop

def make_two_way(singlyll):
    if singlyll == None:
        return (None, None)
    temp = singlyll
    doublyll = TwoWayNode(temp.data)
    temp2 = doublyll
    while temp.next != None:
        temp = temp.next
        new_node = TwoWayNode(temp.data, previous=doublyll)
        doublyll.next = new_node
        doublyll = doublyll.next
    return (temp2, doublyll)

sll = Node(10)
for i in range(9, 0, -1):
    sll = insert(0, i, sll)

temp = sll
while temp != None:
    print(temp.data, end=" ")
    temp = temp.next
print()

(temp2, dll) = make_two_way(sll)

while temp2 != None:
    print(temp2.data, end=" ")
    temp2 = temp2.next
print()

while dll != None:
    print(dll.data, end=" ")
    dll = dll.previous
print()

    
