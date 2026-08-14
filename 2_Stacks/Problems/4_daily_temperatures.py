'''
https://leetcode.com/problems/daily-temperatures
'''

from typing import List

# 1> Brute Force
'''
Time complexity: O(n²)
Space complexity:
O(1) extra space
O(n) space for the output array
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n:
                if temperatures[i] < temperatures[j]:
                    break
                j += 1
                count += 1
            count = 0 if j == n else count
            res.append(count)

        return res

# 2> Stack
'''
Time complexity: O(n)
Space complexity: O(n)
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # array of pair (temp, index)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))

        return res