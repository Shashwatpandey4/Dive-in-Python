class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collect = {}

        for i,n in enumerate(nums):    #enumerate is a built-in functions to keep count of the number of iterations
            diff = target - n
            if diff in collect:
                return [collect[diff],i]
            collect[n] = i