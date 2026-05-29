'''
Count frequencies of characters in "banana"
'''

s = "banana"

freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)