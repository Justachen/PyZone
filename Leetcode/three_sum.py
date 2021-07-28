
class Solution:
	def three_sum(self, nums):
		'''
		nums: list[int]
		rtype: list[tuples that add up to num 0, none duplicates]
		'''
		nums.sort()
		triplets = []
		for i in range(len(nums) - 2):
			current = nums[i]
			self.two_sum(nums, triplets, -current, i + 1)
		return triplets


	def two_sum(self, nums, triplets, target, left):
		right = len(nums) - 1
		while left < right:
			if nums[left] + nums[right] == target:
				triplet = [-target, nums[left], nums[right]]
				if triplet not in triplets:
					triplets.append([-target, nums[left], nums[right]])
				left += 1
				right -= 1
				while nums[left] == nums[left - 1] or nums[right] == nums[right + 1]:
					if nums[left] == nums[left - 1]:
						left += 1
					if nums[right] == nums[right + 1]:
						right -= 1
			elif nums[left] + nums[right] < target:
				left += 1
			else:
				right -= 1

if __name__ == "__main__":
	nums = [-1, 0, 1, 2, -1, -4]
	calc = Solution()
	print(calc.three_sum(nums))
