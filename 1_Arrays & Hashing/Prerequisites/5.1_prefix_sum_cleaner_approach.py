'''
Build a prefix sum array to efficiently 
calculate the sum of elements within a given range.
'''

nums = [3, 1, 4, 2]

# Create prefix array
prefix = [0] * (len(nums) + 1) # Extra leading zero

for i in range(len(nums)):
    # Shift by one position
    prefix[i + 1] = prefix[i] + nums[i]

print(prefix)

def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]

print(range_sum(prefix, 1, 3))