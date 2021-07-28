
class Solution:
	def valid_parentheses(self, string):
		'''
		string: str
		rtype: bool
		'''
		# create a dictionary of the types of opening brackets and closing brackets with the pair
		# create two lists of opening and closing brackets to check what the new char is
		# Then use a queue, opening brackets are just placed in the que and when we see a closing bracket, 
		# It has to match the last opening bracket of the queue for it to be correct
		opening = ['{', '[', '(']
		closing = ['}', ']', ')']
		pairs = {
			'{' : '}',
			'[' : ']',
			'(' : ')',
		}
		q = []

		for i in string:
			if i in opening:
				q.append(i)
			elif i in closing:
				temp = q.pop()
				if pairs[temp] != i:
					return False

		if q:
			return False
		return True







if __name__ == '__main__':
	s1 = "()"
	s2 = "()[]{}"
	s3 = "(]"
	s4 = "([)]"
	s5 = "{[]}"
	test = Solution()
	print(test.valid_parentheses(s5))