'''
Detect duplicates in an array
'''

def has_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True # Duplicate found
        seen.add(num)
    return False # No duplicates
    
# Example
arr = [1, 2, 3, 4, 2]
print(has_duplicates(arr)) # Output: True