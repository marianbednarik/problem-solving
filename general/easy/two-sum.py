"""

https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


def twoSum(nums: [int], target: int) -> [int]:
    d = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff not in d:
            d[num] = index
        else:
            return [d[diff], index]


print(twoSum([2, 5, 12, 7], 9))
