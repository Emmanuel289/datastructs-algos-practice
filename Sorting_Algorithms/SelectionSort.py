"""
The selection sort algorithm repeatedly identifies the smallest
remaining unsorted element and puts it at the end of the sorted portion of the array

E.g input array = ['s' 'e' 'l', 'e', 'c', 't', 'i', 'o', 'n', 's', 'o', 'r', 't']
	output array = ['c' 'e' 'e', 'i', 'l', 'n', 'o', 'o', 'r', 's', 's', 't', 't']
Usage
print(selection_sort(input_array))
Complexity is O(n^2) where n is the length of the array

"""

def selection_sort(arr_input):
	arr_len = len(arr_input)
	
	for i in range(0, arr_len):
		for  j in range(i+1, arr_len):
			if arr_input[j]< arr_input[i]:
				temp = arr_input[i]
				arr_input[i]= arr_input[j]
				arr_input[j]= temp
				
				#or use swap syntax, i.e. arr_input[i], arr_input[j] = arr_input[j], arr_input[i]
				
	
	sorted_arr = arr_input
	
	return sorted_arr


#test 

def test_selection_sort(test_input, sorted_output):
	print(True if selection_sort(test_input)== sorted_output else False)
	
input = [1,7,4,3,10,2]
sorted = [1,2,3,4,7,10]

test_selection_sort(input, sorted)
