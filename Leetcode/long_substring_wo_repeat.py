
class Solution:
	def __init__(self):
		pass

	def longest_substring(self, s):
		'''
		s: string
		rtype: int
		'''

		# create a dictionary
		# have a start and a max_len variable
		# if the current char is in the dictionary, update start
		# check max length of unique chars
		# place the char in dictionary witht the current index

		unique = {}
		start, max_len = 0, 0
		for end in range(len(s)):
			if s[end] in unique:
				start = max(unique[s[end]] + 1, start)
			max_len = max(max_len, end-start+1)
			unique[s[end]] = end
		return max_len

		# given a string, return the longest substring without repeating chars
		# longest = 0
		# data = {}
		# left, right = 0, 0
		# while right < len(s):
		# 	current = s[right]
		# 	if current not in data:
		# 		data[current] = right
		# 	elif current in data:
		# 		if data[current] >= left:
		# 			left = data[current] + 1
		# 			data[current] = right
		# 	print(f'left: {left} - right: {right}')
		# 	longest = max(longest, right - left + 1)
		# 	print(f'longest substring: {longest}')
		# 	right += 1
		# return longest


if __name__ == "__main__":
	s1 = 'abcdef'
	s2 = 'abcabcd'
	s3 = 'deefghed'
	solution = Solution()
	print(solution.longest_substring(s3))

