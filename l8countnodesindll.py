
#Count the number of nodes in a doubly linked list.
#node class
class node:
	#constructor
	def __init__(self,data):
		self.data = data
		self.prev = None
		self.next = None

#linkedlist class
class LinkedList:
	def __init__(self):
		self.head = None

#printing list
	def display(self):
		ele = []
		cur = self.head
		while cur:
			ele.append(cur.data)
			cur = cur.next
		print("Doubly LinkedList: ",ele)

#counting no of elements in the linked list
	def countNodes(self):
		count = 0
		cur = self.head
		while cur:
			count += 1
			cur = cur.next
		print("Count is: ",count)

#initialization
DLL = LinkedList()

#creating nodes 
DLL.head = node(10) 
DLL.head.next = node(20)
DLL.head.next.next = node(30) 

#function calling
DLL.display()
DLL.countNodes()
