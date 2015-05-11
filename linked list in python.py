class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + " " + self.next

class SingleList(object):
    """docstring for SingleList"""
    head = None
    tail = None

    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def show(self):
        print "Printing list:"
        current_node = self.head
        print current_node.data
        while (current_node):
            print "->"+str(current_node.data)
            current_node = current_node.next

    def remove(self, data):
        current_node = self.head
        last_node = current_node
        while current_node:
            if current_node.data == data:
                if current_node == self.head:
                    self.head = current_node.next
                    current_node.next = None
                    print "Node deleted"
                    break
                last_node.next = current_node.next
                current_node.next = None
                print "Node deleted"
                break
            last_node = current_node
            current_node = current_node.next

s = SingleList()
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)
s.remove(50)
s.show()