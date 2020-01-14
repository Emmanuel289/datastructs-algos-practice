class Node(object):
	def __init__(self,value):
		self.value = value  #set this node's value
		self.next  = None   #set the node to point to None

	#Traverse through the LL and print its values
	def traverse_list(node):
		current_node = node  #set current node 

		while current_node is not None:
			print(current_node.value)
			current_node = current_node.next


	#Method 1: Create a linked list by iteration 

	def create_linked_list(input_list):
		"""
		Function to create a linked list 
		@param input_list: a list of integers
		@return: head node of the linked list
		"""
		try:
			head = Node(input_list.pop(0)) #remove the first list item and return as its head

			while (len(input_list)>0):
				current_node = head
				while current_node.next:
					current_node = current_node.next
				current_node.next = Node(input_list.pop(0))

		except IndexError:
				head = None
		return head

	#Method 2: Create a linked list by iteration with more efficiency
	def create_linked_list_better(input_list):
		"""
		@param input_list: a list of integers
		@return: head node of the linked list
		"""
		try:
			head = Node(input_list.pop()) #return the first item as the head
			tail = head  #assign head to tail


			while len(input_list)>0:
				tail.next = Node(input_list.pop()) #return the next node as the tail
				tail = tail.next #update the tail to be the next node

		except IndexError:  #No head
			head = None

		return head

	#Method 3: Create a linked list by iteration with more efficiency
	def create_linked_list_better2(input_list):
		head = None
		tail = None
		for value in input_list:
			if head is None:
				head = Node(value)
				tail = head # when only 1 node, head and tail refer to same node
			else:
		 		tail.next = Node(value) #forward pointer to presnt tail and insert new node
		 		tail = tail.next  #update the tail to be new inserted node
		



#Test Create a LL like this 2->1->4->3->5
head = Node(2)  #Create a head node with value 2
head.next = Node(1)    #Create node with value 1 and link to 2
head.next.next = Node(4)  #create node with value 4 and link to 1
head.next.next.next = Node(3) #create node with value 3 and link to 4
head.next.next.next.next = Node(5) #create node with value 5 and link to 3
#print(head.value)  #prints 2
#print(head.next.value) #prints 1
#print(head.next.next.value) #prints 4
#print(head.next.next.next.value) #prints 3
#print(head.next.next.next.next.value) #prints 5


#Test node traversal function
ll = Node.traverse_list(head)  #Prints all values in the linked list


#Test code for iterator functions for creating linked list
def test_function(input_list, head):
	try:

		if len(input_list)==0:  #if empty list
			if head is not None:  #if head is not null
				print("Fail")
				return
			for value in input_list:
				if head.value!=value:  #if value in list is not head
					print('Fail')
					return
				else:
					head =head.next  #if value is head move head to null
			print("Pass")

	except Exception as e:  #if invalid params, print exception
		print("Fail:" +e)




#test for first create_linked_list method
ll= [1,2,3,4,5,6]
head = Node.create_linked_list(ll)
test_function(ll,head) #Fail
ll =[1]
head = Node.create_linked_list(ll)
test_function(ll,head) #Fail
ll = []
head = Node.create_linked_list(ll) #Fail
test_function(ll,head)



#Test for first create_linked_list_method

ll= [1,2,3,4,5,6]
head = Node.create_linked_list_better(ll)
test_function(ll,head) #Fail
ll =[1]
head = Node.create_linked_list_better(ll)
test_function(ll,head) #Fail
ll = []
head = Node.create_linked_list_better(ll) #Fail
test_function(ll,head)




#Test for second create_linked_list_method

ll= [1,2,3,4,5,6]
head = Node.create_linked_list_better2(ll)
test_function(ll,head) #Fail
ll =[1]
head = Node.create_linked_list_better2(ll)
test_function(ll,head) #Fail
ll = []
head = Node.create_linked_list_better2(ll) #Fail
test_function(ll,head)








