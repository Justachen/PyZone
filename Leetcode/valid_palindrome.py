
class Solution:
	def is_palindrome(self, string):
		'''
		string: str
		rtype: bool
		'''
		# join all characters that are either letters in the alphabet, or nums (isalpha, isnumeric)
		# and set them to lowercase for consistancy
		# then return the new string == reversed new string
		res = "".join(i.lower() for i in string if i.isalpha() or i.isnumeric())
		return res == res[::-1]

if __name__ == "__main__":
	s1 = "A man, a plan, a canal: Panama"
	s2 = "race a car"
	s3 = "racecar"

	answer = Solution()
	print(answer.is_palindrome(s2))