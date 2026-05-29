'''
Implement a hash table with insert, search, update, 
and delete operations using separate chaining.
'''

class HashTable:
    def __init__(self, size=5):
        # Number of buckets
        self.size = size

        # Create empty buckets
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Convert key into bucket index
        return hash(key) % self.size
    
    def insert(self, key, value):
        # Find bucket index
        index = self.hash_function(key)

        # Get bucket list
        bucket = self.table[index]

        # Update if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Otherwise append new pair
        bucket.append((key, value))
    
    def get(self, key):
        # Find bucket
        index = self.hash_function(key)

        # Search bucket
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
            
        return None
    
    def remove(self, key):
        # Find bucket
        index = self.hash_function(key)

        bucket = self.table[index]

        # Find and remove pair
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
            
# Create a hash table
ht = HashTable(size=5)

# Insert some key-value pairs
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)

# Retrieve values
print("apple:", ht.get("apple"))    # Should print 10
print("banana:", ht.get("banana"))  # Should print 20
print("grape:", ht.get("grape"))    # Key not inserted, should print None

# Update a value
ht.insert("apple", 50)
print("apple after update:", ht.get("apple"))  # Should print 50

# Remove a key
ht.remove("banana")
print("banana after removal:", ht.get("banana"))  # Should print None

# Check the internal state of the hash table (optional)
print("HashTable buckets:", ht.table)