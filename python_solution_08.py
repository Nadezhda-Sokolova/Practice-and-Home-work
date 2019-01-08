#I Functions and generators

#1.1

couple_numbers_sum = lambda x, y: x+y
print(couple_numbers_sum(4,5))

#1.2

def sum(x, y):
  action = x+y
  return action

pairs_numbers_sum = sum(4,5)
print(pairs_numbers_sum)

#2 

def cast_to_float(*args):
  sum_of_float_numbers = 0

  for i in args:
    try:
      i = float(i)
      sum_of_float_numbers += i
    except ValueError: i == 0

  return sum_of_float_numbers


sum_of_arguments = cast_to_float(-1,'one',9)
print(sum_of_arguments)

#3 function with list of integer

def double_arguments(i):
  if type(i) == int:
    i*=2
  else: i = None
  #return (i)


list_of_arguments = [1,2,3,4.5,'8']

new_list = list(map(double_arguments, list_of_arguments))
print(new_list)
print(list_of_arguments) #initial list is still stable

#4 

def square(length, width=1):
  return length*width

width = 1

Square1 = square(7)
print(Square1)

Square2 = square (4, 8)
print(Square2)


#5

x = (i for i in range(1,10) if i%2 != 0)
print(x.next())
print(next(x))
print(next(x))


# III Classes

from math import sqrt

def length (x,y):
  r = (sqrt(x**2 + y**2))
  return r

y = 0
x = 0

Coordinates = length (2,2)
print(Coordinates)

Coordinates1 = length (3,3)
print (Coordinates1)



#II Modules and imports

F1 = open('file.py')
F1.close()
F2 = open('file_with_function.py', 'w+')
F2.write('def function(x,y):\n c = x*y\n return c')
F2.close()

import sys

# import of all module

import file_with_function
print(file_with_function.function(9,3))
sys.stdout = open('file.py', 'w')
print('import of all module\n')
print(file_with_function.function(9,3))


# import only function

from file_with_function import function
print(function(6,10))
sys.stdout = open('file.py', 'w')
print('Import of only function', function(6,10))
sys.stdout.close()

# give function another name

sys.stdout = open('file.py', 'w')
from file_with_function import function as new_name_function
print(new_name_function(4,5))
sys.stdout.close()

















