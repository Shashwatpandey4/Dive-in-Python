from typing import List

def containsDuplicate(nums):
        return( len(set(nums))!=len(nums))

containsDuplicate([1,2,3,1])