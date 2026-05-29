'''
Build a prefix sum array to efficiently 
calculate the sum of elements within a given range.
'''

nums = [3, 1, 4, 2]

# Create prefix array
prefix = [0] * len(nums)

# First element
prefix[0] = nums[0]

# Build cumulative sums
for i in range(1, len(nums)):
    # current prefix = previous prefix + current number
    prefix[i] = prefix[i-1] + nums[i]

print(prefix)

def range_sum(prefix, left, right):
    # If started from index 0
    if left == 0:
        return prefix[right]
    
    # Remove unwanted left portion
    return prefix[right] - prefix[left - 1]

print(range_sum(prefix, 1, 3))