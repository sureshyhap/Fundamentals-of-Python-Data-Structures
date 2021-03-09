class Array(object):
    
    def __init__(self, capacity, fill_value=None):
        self.items = []
        for count in range(capacity):
            self.items.append(fill_value)
        if fill_value == None:
            self.logical_size = 0
        else:
            self.logical_size = capacity

    def __len__(self):
        return len(self.items)

    def __str__(self):
        s = ""
        for element in self.items:
            s += (str(element) + " ")
        return s

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        if index < 0 or index >= self.size():
            raise Exception("Index out of bounds")
        return self.items[index]

    def __setitem__(self, index, new_item):
        if index < 0 or index >= self.size():
            raise Exception("Index out of bounds")        
        self.items[index] = new_item

    def size(self):
        return self.logical_size

    def insert_end(self, item):
        if self.size() == len(self):
            self.grow()
        self.items[self.logical_size] = item
        self.logical_size += 1
            
    def grow(self, fill_value=None):
        """ Should only grow if size == capacity """
        items2 = []
        for elem in self.items:
            items2.append(elem)
        for i in range(len(self), len(self) * 2):
            items2.append(fill_value)
        self.items = items2

    def shrink(self):
        if self.size() >= (len(self) / 2):
            return
        items2 = []
        for i in range(len(self) / 2):
            items2 = self.items[i]
        self.items = items2

    def insert(self, index, item):
        if index < 0:
            raise Exception("Out of bounds")
        elif index > self.size():
            index = self.size()
        if self.size() == len(self):
            self.grow()        
        for i in range(self.size(), index, -1):
            self.items[i] = self.items[i - 1]
        self.items[index] = item
        self.logical_size += 1

    def pop(self, index):
        if index < 0 or index >= self.size():
            raise Exception("Out of bounds")
        element = self.items[index]
        for i in range(index, self.size() - 1):
            self.items[i] = self.items[i + 1]
        self.logical_size -= 1
        self.shrink()
        return element

    def __eq__(self, other):
        if isinstance(other, Array) and self.size() == other.size():
            for i in range(self.logical_size):
                if self[i] != other[i]:
                    return False
            return True
        else:
            return False

    def __add__(self, other):
        if self.size() != other.size():
            return
        sum = Array(self.size())
        for i in range(self.size()):
            print(i)
            sum[i] = (self.items[i] + other.items[i])
        return sum
                    
                
            
