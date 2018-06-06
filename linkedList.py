class Node(object):

	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList(object):

	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while (temp):
			print temp.data ,
			temp = temp.next

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def  insertAfter(self,prev_node,new_data):
		if prev_node is None :
			print 'the given previous node must be in Link '
			return

		new_node = Node(new_data)

		new_node.next = prev_node.next
		prev_node.next = new_node

	def append(self,new_data):
		new_node = Node(new_data)

		if self.head is None:
			self.head = new_node
			return

		last = self.head
		while (last.next):
			last = last.next
		last.next = new_node

		# def delNode(self, key):
		# 	temp = self.head
		# 	if (temp is not None):
		# 		if (temp.data == key):
		# 			self.head = temp.next
		# 			temp = None
		# 			return

		# 	while (temp is not None):
		# 		if temp.data == key:
		# 			break
		# 			prev =temp
		# 			temp = temp.next

		# 		if






if __name__ == '__main__':

	llist = LinkedList()

	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	fourth = Node(4)

	llist.head.next = second
	second.next = third
	third.next = fourth
	#fourth.next = None


	llist.append(89)
	llist.printList()
	llist.push(5)
	llist.push(0)
	print '\n'
	llist.printList()
	print '\n'
	llist.append(9)
	llist.printList()
