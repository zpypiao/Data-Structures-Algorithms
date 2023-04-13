class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterater:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration
            
        def __iter__(self):
            return self
        
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = next

    def extend(self, obj):
        for each in obj:
            self.append(each)

    def find(self, obj):
        for n in self:
            if obj == n:
                return True
        else:
            return False
        
    def __iter__(self):
        return self.LinkListIterater(self.head)
    def __repr__(self):
        return '<<'+ ','.join(map(str, self))+'>>'
    
class HashTable:
    