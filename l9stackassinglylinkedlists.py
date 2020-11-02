#Implement stack operation through singly linked list

#node class
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
#stack class as linked list
class Stack:
	def __init__(self):
		self.head = None
		self.tail = None
	#adding
	def push(self,data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	def peek(self):
		l = self.tail.data
		return l
	#deleteing
	def pop(self):
		if self.head is None:
			print("UNDERFLOW")
		else:
			prev = None
			cur = self.head
			while cur:
				prev = cur
				cur = cur.next

			prev.next = None
			cur = None
			self.tail = prev
	#printing stack
	def displayStack(self):
		print("Stack: ")
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
		print()
	
s=Stack()
#function calling
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.displayStack()
print(s.peek())
s.pop()
s.displayStack()

