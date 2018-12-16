
#First task

a = {'one':1, 'two':2 }
b = {'three':3, 'four':4}
a.update(b)
print(a)

#===============================

#Second task 

#1st method for small words

c = 'G od'
d = 'do     g'

c = c.replace(' ','')
#print(c)
d = d.replace(' ','')
#print(d)


import itertools
from itertools import permutations
variation = list(itertools.permutations(c, len(c)))
combinations = [('').join(i) for i in variation]
#print(combinations)

for word in combinations:
  if word.lower( ) == d.lower( ): 
    print ('God and dog are anagram')
    break
else: print ('God and dog are not anagram')

# 2nd Sorted method 


a = 'Clin t Eastwo od' 
b = 'Old Westac  tion'

a = a.replace(' ','')
a = a.upper()
#print(a)
b = b.replace(' ','')
b = b.upper()
#print(b)

a1 = list(sorted(a))
#print(a1)
b2 = list(sorted(b))
#print(b2)

if a1 == b2:
  print('Clint Eastwood and Old Westaction are anagram')
else:
  print('Clint Eastwood and Old Westaction are not anagram')


#==================================


#Third task

def func(x,y):
  num = 5
  if x != y:
    sum = x+y
    if sum == num:
        #print (x, y)
        t = (x, y)
        return(t)
        
    

lst = [6, 1, 2, 25, 8, 2, 3, 4, 3]
num = 5
i = 0
j = 1
#x = [i]
#y = [j]
L = set()


while i < len(lst):
    j = i + 1
    while j < len(lst):

      temporary = func(lst[i], lst[j])
      if temporary != None:

         L.add(temporary)
      j+=1
    i+=1
print(L)





