
#Create a doubly linked list
#node class
class node:
	#constructor
	def __init__(self,data):
		#instances
		self.data = data
		self.prev = None
		self.next = None

#linkedlist class
class LinkedList:
	def __init__(self):
		#initialization
		self.head = None

#printing list
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly LinkedList: ",ele)


DLL = LinkedList()

#creating nodes
DLL.head = node(10) 
DLL.head.next = node(20)
DLL.head.next.next = node(30)


DLL.display()