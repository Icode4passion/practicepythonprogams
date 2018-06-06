class Node(object):
	"""docstring for ClassName"""
	def __init__(self, val, next:"Node"=None):
		self.val = val
		self.next = next


		# function annotation
def has_a_loop(head:Node) -> bool:
		slow , fast = head , head
		while fast is not None and fast.next is not None:
			slow , fast = slow.next , fast.next.next

			if slow == fast:
				return True 

		return False
	  
if __name__ == '__main__':

	node4 = Node(4)
	linked_list = Node(1, Node(2, Node(3, node4)))
	node4.next = linked_list

assert has_a_loop(linked_list)
	 
	 
		
		