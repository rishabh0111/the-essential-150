'''
https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150
'''

from typing import List

'''
Time complexity: O(m + n) for each encode() and decode() function call.
Space complexity: O(m + n) for each encode() and decode() function call.
Where m is the sum of lengths of all the strings and n is the number of strings.
'''
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
