
class Solution:
	def insert(self, intervals, newInterval):
		'''
		intervals: list[list[int]]
		newInterval: list[int]
		rtype: List[List[int]]
		'''

		# What kind of intervals do we need to check for?
		# When an interval is overlapping
		# When an interval is before the new Interval
		# When an interval is after the new Interval
		# After combining an interval, holding onto it to check if it overlaps any other intervals after
		# Since intervals are ordered, once we find an interval that is after the new interval, we can just add the rest


		answer = []
		start, end = 0, 1
		for interval in intervals:
			if interval[end] < newInterval[start]:
				# current interval is not overlapping and is before the new interval
				answer.append(interval)
			elif interval[end] >= newInterval[start] and interval[start] <= newInterval[start] or newInterval[end] >= interval[start] and newInterval[start] <= interval[start]:
				# current interval is overlapping
				newInterval[start] = min(interval[start], newInterval[start])
				newInterval[end] = max(interval[end], newInterval[end])
			elif interval[start] > newInterval[end]:
				# current interval is not overlapping and is after the new interval
				if newInterval not in answer:
					answer.append(newInterval)
				answer.append(interval)
		return answer




if __name__ == "__main__":
	'''
	Insert the new interval into the existing intervals so that there are no overlapping
	intervals! Merge the intervals if neccessary!
	'''
	intervals = [[1,3], [6,9]]
	newInterval = [2,5]

	intervals2 = [[1,2], [3,5], [6,7], [8,10], [12,16]]
	newInterval2 = [4, 8]

	problem = Solution()
	print(problem.insert(intervals2, newInterval2))
