
"""

dict_search() has runtime of O(1) with a space complexity of O(n)
array_search() has runtime of O(n) with a space complexity of O(n)


"""


def dict_search(input_arr, num):
	for index, elem in enumerate(input_arr):
		if num == elem:
			print("{} is in {} at  index {}".format(num, input_arr, index))
		
	return None
		
		
def array_search(input_list, num):
	for index in range(len(input_list)):
		if num ==input_list[index]:
			print("{} is in {} at  index {}".format(num, input_list, index))
	return None
			
		
		
def merge_sort(input_list):
	if len(input_list)<2:
		return input_list
		
	else:
		mid = len(input_list)//2 
		left = input_list[:mid]
		right = input_list[mid:]
		merge_sort(left)
		merge_sort(right)
		
		i = 0
		j = 0
		k = 0
		
		while i < len(left) and j < len(right):
			if left[i]< right[j]:
				input_list[k]= left[i]
				i+=1
			else:
				input_list[k] = right[j]
				j+=1
			k+=1
		
		while i< len(left):
			input_list[k]= left[i]
			i+=1
			k+=1
		while j < len(right):
			input_list[k]= right[j]
			j+=1
			k+=1
		
		return input_list

#Test		
test = [56,35,12,27567,75,53, 209]
num1 = 53
num2 = 27567
#print("The results for binary search are:")
#bin_search(test, num1)
#bin_search(test, num2)

print("array_search gives:")
array_search(test, num1)
array_search(test, num2)


print("dict_search gives:")
dict_search(test, num1)
dict_search(test, num2)


