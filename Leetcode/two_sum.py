class Solution:
	def two_sum(self, nums, target):
		'''
		nums = list[int]
		target = int
		rtype = [int, int]
		'''
		data = {}
		for i in range(len(nums)):
			if nums[i] not in data.keys():
				temp = target - nums[i]
				data[temp] = i 
			else:
				return [data[nums[i]], i]

if __name__=="__main__":
	nums = [2, 7, 11, 15]
	target = 9
	solution = Solution()
	print(solution.two_sum(nums, target))