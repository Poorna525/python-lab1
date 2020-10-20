
#Insert Node at a particular position
#node class
class node:
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None
#linkedlist class
class LinkedList:
	def __init__(self):
		self.head = None

	#inserting node in the middle of the list
	def atPosition(self,pre,data):
		new_node = node(data)
		if self.head == None:
			self.head = new_node
		else:
			cur = self.head
			while cur:
				if cur.data == pre:
					n = cur.next
					cur.next = new_node
					new_node.next = n
					new_node.prev = cur
				cur = cur.next
	#printing elements
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly Linked List: ",ele)


DLL = LinkedList()

#adding nodes
DLL.head = node(10)
DLL.head.next = node(20) 
DLL.head.next.next = node(30)
DLL.atPosition(20,8)
DLL.atPosition(10,5) 
\
DLL.display()