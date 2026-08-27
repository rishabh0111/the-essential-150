'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
'''

from typing import List

# 1> Brute Force
'''
Time complexity: O(n^2)
Space complexity: O(1)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []

# 2> Two Pointers
'''
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
                
        return []
