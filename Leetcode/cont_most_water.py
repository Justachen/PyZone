
'''
Given an array of heights, assume each index width is 1,
return the container with largest area 
'''

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

class cont_most_height:
	def max_area(self, height):
		'''
		height = list[int]
		rtype = int 
		'''
		start = 0
		end = len(height) - 1
		most_water = 0
		while start <= end:
			width = end - start
			length = min(height[start], height[end])
			most_water = max(most_water, width * length)
			if height[start] <= height[end]:
				start += 1
			else:
				end -= 1
		return most_water

if __name__=="__main__":
	answer = cont_most_height()
	print(answer.max_area(height))
