# Two Sum II - Input Array Is Sorted. Given a 1-indexed array of integers numbers that are
# already sorted in non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.
# Length: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def two_sum_ii(numbers, target):
	left, right = 0, len(numbers) - 1
	while left < right:
		if numbers[left] + numbers[right] > target:
			right -= 1
		elif numbers[left] + numbers[right] < target:
			left += 1
		else:
			return [left + 1, right + 1]
