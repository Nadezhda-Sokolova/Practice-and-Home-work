#I Functions and generators
#3 function with list of integer
import random
def new_arguments_added(list_as_argument):
	a = random.randint (-10,-1)
	print(a)
 	list_as_argument.append(a)
 	#return (list_as_argument)


list_of_arguments = [1,2,3,4.5,'8']

new_list = new_arguments_added (list_of_arguments)
print(list_of_arguments) #initial list has been changed by function named is "new_arguments_added"
print(new_list)