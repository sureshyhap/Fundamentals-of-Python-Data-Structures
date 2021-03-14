class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class TwoWayNode(Node):
    def __init__(self, data, next=None, previous=None):
        super(TwoWayNode, self).__init__(data, next)
        self.previous = previous

def length(linked_list):
    """ Assumes at least one element """
    l = 1
    temp = linked_list
    while temp.next:
        l += 1
        temp = temp.next
    return l

def insert(position, item, linked_list):
    if position == 0:
        return Node(item, linked_list)
    if position > length(linked_list):
        position = length(linked_list)
    temp = linked_list
    for i in range(position - 1):
        temp = temp.next
    temp.next = Node(item, temp.next)
    return linked_list
    
def pop(position, linked_list):
    if position < 0 or position >= length(linked_list):
        return (None, None)    
    if linked_list == None:
        return (None, None)
    if length(linked_list) == 1:
        return (None, linked_list.data)
    if position == 0:
        return (linked_list.next, linked_list.data)
    temp = linked_list
    for i in range(position - 1):
        temp = temp.next
    d = temp.next.data
    temp.next = temp.next.next
    return (linked_list, d)
    
