# First exercise - keyerror exception handling

# method throug if 

mydict = {'firstkey':'firstvalue', 'secondkey':'secondvalue'}

a = 'thirdkey'
try:
	print(mydict[a])
except KeyError:
	print ('the key is not in the dictionary - First method')

key = 'forthkey'
#for keys in mydict:
if key in mydict: print ('true', mydict[key])
else: print('the key is not in the dictionary - Second method')

k = 'fifthkey'
d = mydict.get((a), 'the key is not in the dictionary - Third method')
print(d)

# Second exercise - merger two lists
list_1 = ['one', 'two', 'tree']
list_2 = [1, 2, 3]
Joined_lists = dict(zip(list_1, list_2))
print (Joined_lists)

#Third task - dictionary sorting
mydict = {'a':500, 'zz':1, 'cd':23, 'ddd': 321}
all_keys = mydict.keys()
list_of_keys = list(all_keys)
list_of_keys.sort()
for k in list_of_keys: print(k, mydict[k])




