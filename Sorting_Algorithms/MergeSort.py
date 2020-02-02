"""MergeSort is a divide and conquer algorithm that divides a list into equal halves until it has two single elements 
and then merges the sub-lists until the entire list has been reassembled in order. MergeSort can be implemented recursively and its runtime complexity is (O(nlogn))
n is the length of the input array

"""

def mergesort(items):
	#Base case for a single element, return immediately
	if len(items)==1:
		return items
	
	#Else, find the midpoint and split the list into a left and right list
	items_len = len(items)
	
	mid = items_len//2
	
	left = items[:mid] # left subarray
	right = items[mid:] #right subarray
	
	#Call merge sort recursively to update the left and right sublists which compute in O(logn) time
	left = mergesort(left)
	right = mergesort(right)
	
	#Merge the two sublists using the merge function
	return merge(left, right)  #Takes O(n) so in all MergeSort is O(nlogn)
	

def merge(left,right):
	merged_list = [] #list of merged elements
	len_left = len(left)
	len_right = len(right)
	index1 = 0 # index for left
	index2 = 0 # index for right
	while index1 < len_left and index2 < len_right:
		if left[index1]< right[index2]:
			merged_list.append(left[index1])
			index1+=1
		else:
			merged_list.append(right[index2])
			index2+=1
	#Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
	merged_list+= left[index1:]
	merged_list+= right[index2:]
	return merged_list
	

#Test
test_input1 =[8, 3, 1, 7, 0, 10, 2]	
test_input2  = [2,68,7,11,34,5,67,29]
print(mergesort(test_input1)) #answer =>[0, 1, 2, 3, 7, 8, 10]
print(mergesort(test_input2)) #answer => [2,5,7,11,29,34,67,68]
