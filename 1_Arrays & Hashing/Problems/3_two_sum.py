'''
https://leetcode.com/problems/two-sum/
'''

# Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# Hash Map (Two Pass)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        # Map each value to its index for constant-time complement lookups.
        for i, n in enumerate(nums):
            indices[n] = i
        
        # Find a number whose complement exists at a different index.
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []


# Hash Map (One Pass)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i