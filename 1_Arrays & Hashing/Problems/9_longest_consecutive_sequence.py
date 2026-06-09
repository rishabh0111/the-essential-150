'''
https://leetcode.com/problems/longest-consecutive-sequence
'''

from typing import List
from collections import defaultdict

# 1> Brute Force
'''
Time complexity: O(n²)
Space complexity: O(n)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
    
# 2> Sorting
'''
Time complexity: O(n log n)
Space complexity: O(1) or O(n), depending on the sorting algorithm.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()

        res = 0
        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and curr == nums[i]:
                i += 1
            curr += 1
            streak += 1
            res = max(res, streak)
        return res

# 3> Hash Set
'''
Time complexity: O(n)
Space complexity: O(n)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0
        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest
    
# 4> Hash Map
'''
Time complexity: O(n)
Space complexity: O(n)
Demonstrates an interval-merging technique 
where each number updates only the sequence boundaries, 
maintaining O(n) time complexity.
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                # Update left boundary
                mp[num - mp[num - 1]] = mp[num]
                # Update right boundary
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res