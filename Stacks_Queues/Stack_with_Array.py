# Implement a Stack using an Array

# Define a Stack class

class Stack:

    def __init__(self, initial_size=10):
        self.arr = [0 for el in range(initial_size)]  # initialize an array of zeros with length of the initial size
        self.next_index = 0  # next index in stack
        self.num_items = 0  # initial number of elements

    # Implement a push method that adds an item on top of the stack
    def push(self, item):
        self.arr[self.next_index] = item
        self.next_index += 1  # increment index after adding item
        self.num_items += 1  # increment number of items in stack\

    # Implement a push method to check for full capacity
    def push_check(self, item):
        if self.next_index == len(self.arr):  # Check if stack is already full
            print("Out of space! Increasing array capacity ...")
            self.handle_capacity()  # call function to handle full capacity
        self.arr[self.next_index] = item
        self.next_index += 1
        self.num_items += 1
    # Implement a method that handles a stack that's already at full capacity
    def handle_capacity(self):
        temp_copy = self.arr  # save temporary copy of array in stack
        self.arr = [0 for el in range(2 * len(self.arr))]  # double the current size of the stack
        for index, value in enumerate(temp_copy):
            self.arr[index] = value

    # Implement a method that returns the current size of the stack
    def size(self):
        return self.next_index

    # Implement a method that returns True if the stack is empty and False otherwise
    def is_empty(self):
        return self.next_index==0
     #Implement the pop method that removes the first item and returns the item

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_items -= 1
        return self.arr[self.next_index]

# Test push()
foo = Stack()  # create stack
foo.push("Test Item!")
print(foo.arr)
print("Pass" if foo.arr[0] == "Test Item!" else "Fail")

# Test push_check()
foo = Stack()
for num in range(12):  # will cause the array to double in size
    foo.push_check(num)
print(foo.arr)
print(len(foo.arr))
print("Pass" if len(foo.arr) == 20 else "Fail")  # will Pass because the number of added items
# will exceed the initial size of 10, causing the array to be doubled t0 20


# Test size() and isempty()
foo = Stack()
print(foo.size())  # returns 0
print(foo.is_empty())  # returns True
foo.push("Test item")

print(foo.size())  # returns 1
print(foo.is_empty())  #returns False

#Test pop
foo= Stack()
foo.push(1)
print(foo.arr) #Should return [1,......,0]
print(foo.pop()) #Should return 1 , i.e pushed item
print(foo.pop()) # Should return None