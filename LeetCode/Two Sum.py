"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.+
"""

def twoSum(list, target):
    for i in list:
        for j in list:
            if j != i and j == (target - i):
                return [list.index(i), list.index(j)]

list = [2,10,25,30,50]
target = 80
x = twoSum(list, target)
print(x)
