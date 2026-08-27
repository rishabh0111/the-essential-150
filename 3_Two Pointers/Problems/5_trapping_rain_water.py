'''
https://leetcode.com/problems/trapping-rain-water
'''

from typing import List

# 1> Brute Force
'''
Time complexity: O(n^2)
Space complexity: O(1)
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)

        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i+1, n):
                rightMax = max(rightMax, height[j])

            res += min(leftMax, rightMax) - height[i]

        return res

# 2> Prefix & Suffix Arrays
'''
Time complexity: O(n)
Space complexity: O(n)
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]

        return res

# 3 > Two Pointers
'''
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1

        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res