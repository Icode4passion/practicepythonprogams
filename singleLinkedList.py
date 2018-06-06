# # class Node(object):
# #     def __init__(self, data=None,next_node=None):
# #         self.data = data
# #         # pointer set to None as the first node inserted into the list will have nothing to point at all
# #         self.next_node = next_node
# #     #one that returns a stored data
# #     def get_data(self):
# #         return self.data
# #     #method that returns next node
# #     def get_next(self):
# #         return self.next_node
# #     #finally a method to reset the pointer to a new node.
# #     def set_next(self):
# #         self.next_node = new_next
# #
# #
# # class LinkedList(object):
# #     def __init__(self, head=None):
# #         self.head = head
# #
# #     def insert(self,data):
# #         new_node = Node(data)
# #         new_node.set_next(self.head)
# #         self.head = new_node
# #
# #
# class Node(object):
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None
#
# class LinkedList(object):
#
#     def __init__(self):
#         self.head = None
#
#     def add(self , data):
#
#         node = Node(data)
#
#         if self.head == None:
#             self.head = node
#         else :
#             node.next = self.head
#             node.next.prev = node
#             self.head = node
#
#
# ll = LinkedList()
# ll.add('a')
# ll.add('b')
# ll.add('1')
# print ll




class Node(oject):
    def __init__(self,data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self,data):
        self.size = self.size+1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def size(self):
        return self.size

    def insertEnd(self,data):
        self.size = self.size +1
        newNode = Node(data)
        actualNode =self.head

        while actualNode.nextNode == None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def Traverse(self):
        actualNode = self.head

        while actualNode is not None:
            print '%d' %actualNode.data
            actualNode = actualNode.nextNode

    def remove(self,data):
        if self.head is None:
            return
        self.size = self.size -1
