#Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

from Stack_List import Stack


def reverse_string(mystr):
	s1 = Stack() #empty stack
		
	rstr = '' #empty reverse string
	
	for index in range(len(mystr)):
		s1.push(mystr[index])
	
	while not s1.isEmpty():
		rstr+=s1.pop()
	return rstr
		
		
		
#Test
input_strs = ['cat', 'dog', 'chicken', 'hen', 'goat', 'hippoppotamus']

rev_strs = ['tac', 'god', 'nekcihc', 'neh', 'taog', 'sumatoppoppih']


for index in range(len(input_strs)):
	print(reverse_string(input_strs[index]))

for index in range(len(input_strs)):
	print(True if reverse_string(input_strs[index])== rev_strs[index] else False)