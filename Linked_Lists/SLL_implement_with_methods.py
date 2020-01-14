#Implementation of a Singly Linked List with methods for common operations
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Create a LinkedList Class as a wrapper for the nodes themselves
class LinkedList():
	def __init__(self):
		self.head = None

	#Define an append method to add to the linkedlist at the end(tail). does it in linear time

	def append(self,value):
		if self.head ==None:
			self.head = Node(value)
			return 


		node = self.head #set current node to head
		while node.next:
			node = node.next #forward pointer to next node
		node.next = Node(value) #create node that is pointed to
		return

	#Define a method that converts a linked list back to a python list. Does it in linear time

	def to_list(self):
		node_values = [] #initialize an empty list
		node = self.head #start with the head node
		while node:
			node_values.append(node.value) #append each node value
			node = node.next #update the node value by moving to the next node and repeat
		return node_values

#test creating and appending to an SLL
linked_list = LinkedList()  #Create an SLL
linked_list.append(1) #append nodes to the SLL
linked_list.append(2)
linked_list.append(4)
node = linked_list.head  #create a new head object with the LinkedList wrapper
while node:
	print(node.value) #print current node value
	node= node.next  #advance to the next node and repeat print operation

#test converting an SLL into a python list

linked_list = LinkedList()
linked_list.append(3)
linked_list.append(2)
linked_list.append(-1)
linked_list.append(0.2)

print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")
