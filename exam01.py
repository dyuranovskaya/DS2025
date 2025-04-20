class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node(50)
node2 = Node(100)
node3 = Node(200)

node1.next = node2
node2.next = node3
current = node1
while current:
    print(current.data)
    current = current.next
