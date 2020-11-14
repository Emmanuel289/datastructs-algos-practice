"""Implement a Stack with a Python List
Provide the basic stack operations: check if its empty, push/pop items to/from the stack, check the size of the stack, peek the top of the stack

"""

class Stack:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return self.items ==[]  # or return len(self_items) ==0
		
	def push(self, item):
		self.items.append(item)
		
	def pop(self):
		return self.items.pop()
	
	def peek(self):
		return self.items[-1]  # or return self.items[len(self.items) -1]
		
	def size(self):
		return len(self.items)
		
	def disp(self):
		index = len(self.items)-1
		
		while index >=0:
			if index == len(self.items)-1:
				print("Top of the stack is: {}. The remaining items in the stack are: \n ".format(self.items[index]))
			elif index ==0:
				print("Bottom of stack is: {}".format(self.items[index]))
				
			else:
				print(self.items[index])
			index-=1
		

		

#Test

# s1 = Stack()
# animals = ['cat', 'dog', '', True, False, None, 'orangutang', 'chicken']

# for animal in animals:
	# s1.push(animal)
	
# s1.disp()