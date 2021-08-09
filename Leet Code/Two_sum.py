'''
problem link = https://leetcode.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collect = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in collect:
                return [collect[diff],i]
            collect[n] = i