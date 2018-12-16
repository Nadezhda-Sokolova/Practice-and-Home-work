#
with open('pushkin.txt', 'r') as f:
                result = {}
                for line_num, line in enumerate(f.readlines(), start=1):
                                result[line_num] = len(line)
 
print (result)



#====== work under mistakes
F = open('pushkin.txt', 'r')
text = F.readlines()
#print(text)

L = []
number = 0
for (number, item) in enumerate (text):
  d = (number+1, len(item))
  L.append(d)
#print(L)
New_dictionary = dict(L)
print(dict(New_dictionary))

F.close()

# First task 
#(including symbol of end string)

F = open('pushkin.txt', 'r')
text = F.readlines()
#print(text)

keys = range(len(text))
keys_list = [i+1 for i in keys]
#print(keys_list)

values_list = []

for line in open('pushkin.txt'): 
  values_list.append(len(line))
#print(values_list)

D = dict (zip(keys_list,values_list))
print(D)

F.close()

#Second task
#Collections: counter


lst = [1, 6, 1, 2, 25, 8, 2, 3, 4, 3]

import collections
from collections import Counter
c = collections.Counter(lst)
print(c)

#Third task

lst = [6, 1, 2, 25, 8, 2, 3, 4, 3]
lst2= list(map(lambda x: x*2, lst))
print(lst2)

lst3 = list(filter(lambda x: x > 10, lst2))
print(lst3)

sum = reduce(lambda x,y: x + y, lst3)
print(sum)








