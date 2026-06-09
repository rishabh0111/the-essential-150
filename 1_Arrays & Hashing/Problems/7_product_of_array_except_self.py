'''
https://leetcode.com/problems/product-of-array-except-self/
'''

from typing import List

# 1> Brute Force
'''
Time complexity: O(n²)
Space complexity:
O(1) extra space.
O(n) space for the output array.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if j == i:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res
        
# 2> Division
'''
Time complexity: O(n)
Space complexity:
O(1) extra space.
O(n) space for the output array.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt += 1

        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
                
        return res
    
# 3> Prefix & Suffix
'''
Time complexity: O(n)
Space complexity: O(n)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n

        pref[0] = suff[n - 1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n-2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res
    
# 4> Prefix & Suffix (optimal)
'''
Time complexity: O(n)
Space complexity:
O(1) extra space.
O(n) space for the output array.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res