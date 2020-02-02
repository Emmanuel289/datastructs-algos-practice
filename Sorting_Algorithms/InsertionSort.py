"""
Insertion Sort algorithm for sorting a list of elements in ascending and descending order
"""

def insertion_sort_ascending(input): #[5,1,3,2,8,6,9,4,7]
	input_len = len(input) #9
	
	for i in range(1, input_len): # i=1, 2, 3,
		j =i #j=1,2,3
		while (j >0 and input[j] < input[j-1]):  #element at present index is less than element in previous index. 1 < 5, 3 <5, 3>1, 2 <5, 2 <3, 2>1
			temp = input[j] #save present element, temp = 1, 3, 2, 2
			input[j]= input[j-1] #assign previous element to present element  input[1] =5, input[2]=5, input[3]= 5, input[2]=3
			input[j-1]= temp #assign present element to previous element input[0]=1, input[1]=3, input[2]=, input[1]=2
			j-=1 #[1,5,3,2,8,6,9,4,7], [1,3,5,2,8,6,9,4,7], j=1, [1,3,2,5,8,6,9,4,7], j=2, [1,2,3,5,8,6,9,4,7] , j =1 
	sorted_input = input
	return sorted_input


def insertion_sort_descending(input): #[5,1,3,2,8,6,9,4,7]
	input_len = len(input) #9
	
	for i in range(1, input_len): #i =1,2,3,4
		j =i #j=1,2,3,4
		while (j >0 and input[j] > input[j-1]):  #element at present index is greater than element in previous index. 1 <5,3 >1, 2>1, 2<3, 8 >1, 8 >2, 8 >3, 8 >5
			temp = input[j] #temp = 3,2, 8, 8,8,8
			input[j]= input[j-1] #input[2]=1, input[3]=1, input[4]=1, input[3] = 2, input[2]=3, input[1]=5
			input[j-1]= temp  #input[1]=3, input[2]=2, input[3]=8, input[2]=8, input[1]=8, input[0]=8
			j-=1 #j=1, [5,3,1,2,8,6,9,4,7], j=2, [5,3,2,1,8,6,9,4,7], j=3, [5,3,2,8,1,6,9,4,7], j=2, [5,3,8,2,1,6,9,4,7], j=1, [5,8,3,2,1,6,9,4,7], j=0, [8,5,3,2,1,6,9,4,7]
	sorted_input = input
	return sorted_input

			
#Runtime complexity for insertion sort is O(n^2) in the worst case. Explanation below
#For n = 1, 1 ops
#For n = 2, up to 1+2 ops
#For n = 3, up to 1+2+3 ops
#For general n, up to 1+2+3+...+n ops = n(n+1)/2 ops = (n^2+n)/2 = O(n^2)
	
	
	
#Test
input1 = [5,1,3,2,8,6,9,4,7]
correct_output1a = [1,2,3,4,5,6,7,8,9]
correct_output1d = [9,8,7,6,5,4,3,2,1]


input2 = [18,20,14,16,10,12,6,8,2,4,0]
correct_output2a = [0,2,4,6,8,10,12,14,16,18,20]
correct_output2d = [20,18,16,14,12,10,8,6,4,2,0]

print(insertion_sort_ascending(input1)) #Good
print(insertion_sort_descending(input1))
print(insertion_sort_ascending(input2)) #Good
print(insertion_sort_descending(input2)) #Good
def test_insertion_sort(test, correct_as,correct_de):
	print("Pass" if insertion_sort_ascending(test)==correct_as and insertion_sort_descending(test)==correct_de else "Fail")
	
	

test_insertion_sort(input1, correct_output1a,correct_output1d)
test_insertion_sort(input2, correct_output2a, correct_output2d)