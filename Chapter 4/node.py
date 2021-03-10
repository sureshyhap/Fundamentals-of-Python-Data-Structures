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


##########################
def insert(position, item, linked_list):
    temp = linked_list
    for i in range(position):
        temp = temp.next
    return Node(item, temp)
############################33

    
