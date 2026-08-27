'''
https://leetcode.com/problems/container-with-most-water
'''

from typing import List

# 1> Brute Force
'''
Time complexity: O(n^2)
Space complexity: O(1)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                res = max(res, min(height[i], height[j]) * (j - i))
        return res

# 2> Two Pointer
'''
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        l, r = 0, len(height) - 1

        while l < r:
            res = max(res, min(height[l], height[r]) * (r-l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return res