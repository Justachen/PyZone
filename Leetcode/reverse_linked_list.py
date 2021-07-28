
class Node:
	def __init__(self, val, nxt = None):
		self.val = val
		self.nxt = nxt

class LinkedList:
	def __init__(self, head):
		self.head = head
	
	def print_list(self):
		temp = self.head
		print("List begins: ")
		while temp:
			print(temp.val)
			temp = temp.nxt
		print("\n")

class Solution(object):
	def reverse_list(self, head):
		'''
		type head: node
		rtype: node
		'''
		current, prev, nxt = head, None, None
		while current:
			nxt = current.nxt
			current.nxt = prev
			prev = current
			current = nxt
		return prev

if __name__=='__main__':
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n1.nxt = n2
	n2.nxt = n3
	n3.nxt = n4

	llist = LinkedList(n1)

	llist.print_list()
	answer = Solution()
	llist.head = answer.reverse_list(llist.head)
	llist.print_list()



