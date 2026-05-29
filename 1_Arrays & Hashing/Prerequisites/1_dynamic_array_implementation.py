'''
Implement a DynamicArray class in Python 
that supports append, automatic resizing, 
get, set, pop, and printing the current elements.
'''

class DynamicArray:
    def __init__(self):
        # Current number of actual elements
        self.size = 0

        # Total capacity of allocated memory
        self.capacity = 2

        # Underlying storage
        self.arr = [None] * self.capacity

    def append(self, value):
        # If array is full, resize first
        if self.size == self.capacity:
            self.resize()
        
        # Put value at the next available position
        self.arr[self.size] = value

        # Increase element count
        self.size += 1
    
    def resize(self):
        # Double the capacity
        self.capacity *= 2

        # Create new larger array
        new_arr = [None] * self.capacity

        # Copy old values into new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        
        # Replace old array
        self.arr = new_arr

    def get(self, index):
        # Prevent invalid address
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        # Direct indexing is O(1)
        return self.arr[index]

    def set(self, index, value):
        # Prevent invalid address
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        # Replace value
        self.arr[index] = value

    def pop(self):
        # Can't remove from empty array
        if self.size == 0:
            raise IndexError("Pop from empty array")
        
        # Get last value
        value = self.arr[self.size - 1]

        # Optional cleanup
        self.arr[self.size - 1] = None

        # Reduce size
        self.size -= 1

        return value

    def print_array(self):
        # Print only actual elements
        print(self.arr[:self.size])

cars = DynamicArray()

print("Size of array: ", cars.size)
print("Capacity of array: ", cars.capacity)
cars.print_array()

cars.append(11)
cars.append(22)
cars.print_array()

cars.append(33)
print("Capacity of array after resize: ", cars.capacity)
cars.print_array()

cars.set(0, 13)
cars.print_array()

print(cars.get(1))

cars.pop()
cars.print_array()