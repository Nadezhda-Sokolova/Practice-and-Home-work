#Lists and list comprehensions

#Second task

def phrase(i):
	substr = "one"
	if substr in i:
		return True
	else:
		return False

L = ['one', 'two', 'oneandtwo', 'three', 'none', 'four']
L1 = filter(phrase,L)
print(L1)

L2 = [i for i in L if i not in L1]
print (L2)

#Third task
S = list(range(11))
exec4 = [a for a in S if a % 2 == 0]
print (exec4)

#Forth task
L = list(range(16))
exec5 = [i for i in L if i % 3 == 0]
print (exec5)

#Fifth task
S = list(range(11))
exec6 = [i * 10 for i in exec4]
print (exec6)




#Strings

#Second task
S2 = 'Anfiska is name of my cat'
print(S2)
S2.split(' ') 
#print (S2)
S3 = S2.split(' ')[::-1]
#print (S3)
S4 = ' '.join(S3)
print (S4)

#Third task

import random

name1 = ['Alice', 'Hloe', 'Marilin', 'Jane']
random_name_1 = (random.choice(name1))
#print (random_name_1)

name2 = ['Bob', 'Dick','Tom', 'Alexander']
random_name_2 = (random.choice(name2))
#print (random_name_2)

relations = ['hate', 'love', 'indifferent', 'takes care of']
random_relations = (random.choice(relations))
#print (random_relations)


S7 = '{0} and {1} {2} each other'.format(random_name_1, random_name_2, random_relations)
print (S7)