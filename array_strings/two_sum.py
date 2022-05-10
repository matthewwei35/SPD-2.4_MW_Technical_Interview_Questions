# Given an array a of n numbers and a target value t, find two numbers whose sum is t.
# Example: a=[5, 3, 6, 8, 2, 4, 7], t=10  ⇒  [3, 7] or [6, 4] or [8, 2]

# Clarifying Questions:
# Would zero be included and negative numbers?
# Would we need to return multiple answers to the target value?
# Do we want to return a boolean or two numbers?

# Naive Solution:
# Have two loops, we just add all the numbers from one loop to the other until we find the target. If we don’t return 0. O(n)?

def two_sum(arr, t):
	for x in arr:
		for y in arr:
			if (x + y == t):
				return [x, y]
