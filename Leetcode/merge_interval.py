class Solution:
	def merge(self, intervals):
		'''
		intervals: List[List[Int]]
		rtype: List[List[Int]]
		### Combine the intervals so that there are none overlapping
		'''

		# Intervals are ordered
		# We have to check two intervals at a time and see if there are any overlapping intervals between them
		# Two pointers, current and next
		# If current doesn't overlap the next, append current to the answer array and then set current to next
		# If current does overlap with next, then combine them and update current to the new megerged interval
		# Increment next to the next interval. 
		
		if len(intervals) <= 1:
			return intervals

		answer = []
		start, end = 0, 1
		current, nxt = 0, 1

		current_interval = intervals[current]
		next_interval = intervals[nxt]

		
		while nxt <= len(intervals) - 1:
			if current_interval[end] < next_interval[start]:
				answer.append(current_interval)
				if nxt == len(intervals) - 1:
					answer.append(next_interval)
					break
			elif current_interval[end] >= next_interval[start]:
				current_interval[start] = min(current_interval[start], next_interval[start])
				current_interval[end] = max(current_interval[end], next_interval[end])
				if nxt == len(intervals) - 1:
					answer.append(current_interval)
					break

			current += 1
			nxt += 1

			if current_interval in answer:
				current_interval = intervals[current]
			next_interval = intervals[nxt]
		return answer





if __name__ == "__main__":
	intervals = [[1,3], [2,6], [8,10], [15,18]]
	intervals2 = [[1,4], [4,5]]

	problem = Solution()
	print(problem.merge(intervals2))