'''
https://leetcode.com/problems/3sum
'''

# 1> Brute Force
'''
Time complexity: O(n^3)
Space complexity: O(m), plus the space used by the sorting algorithm.
Where m is number of unique triplets
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        nums.sort() # removes dupliation of triplets
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k])) # push tuple to set
        return [list(i) for i in res] # convert back to lists

# 2> Two Pointers
'''
Time complexity: O(n^2)
Space complexity: O(1), plus the space used by the sorting algorithm.
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res