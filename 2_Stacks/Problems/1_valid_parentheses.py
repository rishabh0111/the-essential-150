'''
https://leetcode.com/problems/valid-parentheses
'''

# 1> Brute Force
'''
Time complexity: O(n²)
Space complexity: O(n)
'''
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
    
# 2> Stack
'''
Time complexity: O(n)
Space complexity: O(n)
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', '}' : '{', ']' : '['}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False