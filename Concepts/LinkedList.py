from collections import deque

data = {}
data['a'] = 1
data['b'] = 2
data['c'] = 3

def print_test(data):
	for i in data:
		print(i, data[i])

#print_test(data)

class Node:
	# Creates single double facing nodes
	def __init__(self, val, prev=None, nxt=None):
		self.val = val
		self.prev = prev
		self.nxt = nxt

class LinkedList:
	# Doubly linked list
	def __init__(self, start, end=None):
		self.start = start
		self.end = end or start


	def add_left(self, curr_node):
		self.start.prev = curr_node
		curr_node.nxt = self.start
		self.start = curr_node


	def pop_left(self):
		popped_node = self.start
		self.start = popped_node.nxt

		# Clean start node
		self.start.prev = None

		# Clean up popped node
		popped_node.nxt = None
		return popped_node.val


	def add_right(self, curr_node):
		self.end.nxt = curr_node
		curr_node.prev = self.end
		self.end = curr_node


	def pop_right(self):
		popped_node = self.end
		self.end = popped_node.prev

		# clean end node
		self.end.nxt = None

		# clean pooped node
		popped_node.prev = None 
		return popped_node.val

n1 = Node(1)
n2 = Node(4)
n3 = Node(3)
n4 = Node(8)

llist = LinkedList(n1)
llist.add_right(n2)
llist.add_left(n3)
llist.add_right(n4)

print('start: ', llist.start.val)
print('end: ', llist.end.val)
print('popped: ', llist.pop_right())
print('end: ', llist.end.val)

def queue():
	q = deque()
	q.append('a')
	q.append('b')
	q.append('c')
	temp = q.popleft()
	print(q)

 # queue()

class que(object):
 	def __init__(self, que = []):
 		self.que = que 

x = que()
x.que.append('a')
x.que.append('b')
x.que.append('c')
# print(x.que)