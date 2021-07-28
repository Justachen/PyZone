
class Solution:
	def __init__(self):
		pass

	def char_replacement(self, string, k):
		'''
		string: str
		k: int
		rtype: int
		'''
		### Return the length of the longest substring containing the same character
		### Given a string and a int k, You can replace k chars with any other to create the longest substring

		# 1. We have to iterate through the string and keep track of the longest continous substring of the 
		# 	 same chars + k extra chars

		max_len, max_so_far = 0, 0
		data = {}
		start = 0
		for end in range(len(string)):
			if string[end] not in data:
				data[string[end]] = 0
			data[string[end]] += 1
			max_so_far = max(max_so_far, data[string[end]])
			if end - start + 1 - max_so_far > k:
				data[string[start]] -= 1
				start += 1
			max_len = max(max_len, end - start + 1)
		return max_len




if __name__ == "__main__":

	s1 = 'ABAB'
	s2 = 'AABABBA'
	s3 = 'AAAABBB'
	k1 = 2
	k2 = 1
	k3 = 2

	solution = Solution()
	print(solution.char_replacement(s1, k1))
