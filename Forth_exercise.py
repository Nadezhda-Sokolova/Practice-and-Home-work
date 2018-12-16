# 1 TASK
#Reversed string via cycle

string = 'Test of reverse string via cycle'
reversed_string = ''

l = len(string)
#print(l)

while l > 0:
  reversed_string += string [(l-1)]
  #print(reversed_string)
  l -= 1
print (reversed_string)


#2 TASK
# All posible letters combinations in string

# First method with itertools

line = 'abc'

import itertools
from itertools import permutations
t = list (itertools.permutations(line, len(line)))
#print(t)

combinations = [''.join(i) for i in t ]
print(combinations)

