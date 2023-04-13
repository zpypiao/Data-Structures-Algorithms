class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def insert(self, node, lo):
        i = 0
        while True:
            if i == lo:
                node

def creatnode_by_list(li, reverse=False):
    head = tail = Node(li[0])
    if reverse:
        for ele in li[1:]:
            node = Node(ele)
            node.next = head
            head = node
    else:
        for ele in li[1:]:
            node = Node(ele)
            tail.next = node
            tail = node
    return head

def print_node(node):
    while node:
        print(node.item)
        node = node.next

li = [1, 5, 6, 8]

node = creatnode_by_list(li, True)
print_node(node)