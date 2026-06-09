'''
https://leetcode.com/problems/valid-anagram/
'''

# 1> Sorting
'''
Time complexity: O(n log n + m log m)
Space complexity: O(1) or O(n + m), depending on the sorting algorithm.
Where n is the length of string s and m is the length of string t.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

# 2> Hash Map
'''
Time complexity: O(n + m)
Space complexity: O(1) since we have at most 26 different characters.
Where n is the length of string s and m is the length of string t.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s, freq_t = {}, {}

        for i in range(len(s)):
            freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
            freq_t[t[i]] = 1 + freq_t.get(t[i], 0)

        return freq_s == freq_t
