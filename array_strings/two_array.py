# Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
# Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]

# Clarifying Questions:
# Is the length of the two arrays isn’t the same?
# Are we returning multiple possible values or just one?
# Are we returning the first occurrence?
# What’s considered close, 1-2 digits away?

# Naive Solution:
# Have two loops, add one number to another from each loop, and if within 1-2 digits away, if they are close, return the two numbers.
