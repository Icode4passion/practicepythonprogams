class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class LList(object):
	def __init__(self):
		self.head = None

	
	def insertAtHead(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insertAtEnd(self,new_data):
		new_node = Node(new_data)
		if self.head is None :
			self.head = new_node
			return
		else :
			last = self.head
			while(last.next):
				last = last.next # 5. Else traverse till the last node
			last.next = new_node

	def getCount(self,node):
		if(not node):
			return 0
		else :
			return 1 + self.getCount(node.next)

	def count(self):
		return self.getCount(self.head)

	def lent(self):
		temp = self.head
		lent = 0
		while (temp):
			lent += 1
			temp = temp.next
		return lent

	def printList(self):
		temp = self.head
		while(temp):
			print('{}'.format(temp.data))
			temp = temp.next

	def delHead(self):
		self.head = self.head.next

	def search(self,data):
		temp = self.head
		while(temp is not None):
			if (temp.data == data):
				return temp

			temp = temp.next
		return None

	def reverse(self):
		prev = None
		temp = self.head
		while (temp is not None):
			next = temp.next
			temp.next = prev
			prev = temp
			temp = next
		self.head = prev
		
	# def delNode(self,position):
	# 	if self.head = None:
	# 		return
	# 	temp = self.head

	# 	if position == 0:
	# 		temp = temp.next
	# 		temp =None
	# 		return
	# 	for i in range(position - 1):
	# 		temp = temp.next

	def swap()




if __name__ == '__main__':
	   
	   llist = LList()
	   # n1 = Node(1)
	   # n2 = Node(2)
	   # n3 = Node(3)
	   # llist.head = n1
	   # n1.next = n2
	   # n2.next = n3
	   # n3.next = None
	   # llist.insertAtHead(1)
	   #llist.insertAtHead(2)
	   # llist.insertAtEnd(8)
	   # llist.insertAtHead(3)
	   # llist.insertAtEnd(18)
	   llist.insertAtHead(4)
	   llist.insertAtHead(11)
	   llist.insertAtHead(12)
	   llist.insertAtHead(13)
	   llist.insertAtHead(14)
	   llist.insertAtHead(15)
	   llist.insertAtHead(16)
	   llist.insertAtHead(17)
	   llist.insertAtHead(18)
	   llist.printList()
	   print('********')
	   llist.reverse()
	   llist.printList()
	   # print (llist.count())
	   # print (llist.lent())
	   # print('del')
	   # llist.delHead()
	   # print (llist.lent())
	   # print('del')
	   # llist.delHead()
	   # print (llist.lent())
	   # print (n2.data,n2.next)
	   #print ('Found {}'.format(llist.search(5)))