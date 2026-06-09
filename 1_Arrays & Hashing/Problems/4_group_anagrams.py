'''
https://neetcode.io/solutions/group-anagrams
'''

from typing import List
from collections import defaultdict

# 1> Sorting
'''
Time complexity: O(m * n log n)
Space complexity: O(m * n)
Where m is the number of strings and n is the length of the longest string.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
    
# 2> Hash Map (Frequency Count)
'''
Time complexity: O(m * n)
Space complexity:
O(m) auxiliary space, excluding the returned output.
O(m * n) total space if the output groups are counted.
Where m is the number of strings and n is the length of the longest string.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())