#1

def extension_verification(a_file):
  if a_file[-3:] in extensions: 
    print('Yes, this extension is allowed')
  else: print('No, this extention isn''t allowed')


extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
file = extension_verification('smilt.gif')


#2 

def checking_prefix(arg_list):
  new_list = [all(x[i] == x[i+1] for i in range(len(x)-1)) for x in zip(*arg_list)]
  return (arg_list[0][:new_list.index(0) if new_list.count(0) > 0 else len(new_list)])



L1 = ['flower','flo','flight']
L2 =  ["dog","racecar","car"]
the_same_long_prefix = checking_prefix(L1)
print('There is common prefix:')
print(the_same_long_prefix)

the_same_long_prefix = checking_prefix(L2)
print('There isn''t common prefix!')
print(the_same_long_prefix)


#3

def searching_number_or_position(a_list, a_x):
  left = 0
  right = len(a_list)-1
  medium = int((right+left)/2)
  while a_list[medium] != a_x and left < right:
    # print("left " + str(left))
    # print("right " + str(right))
    # print("medium " + str(medium))
    if a_x > a_list[medium]:
      left=medium+1
    else:
      right = medium-1
    medium = int((right+left)/2)

  if a_list[medium] == a_x:
    return (medium)
  elif a_list[medium] > a_x:
    return (left)
  else:
    return (right)
    


Li_st = [-1,2,3,5,6,9,10,11,13] 
x = -7
y = 12
z = 6

answer1 = searching_number_or_position (Li_st, x)
print(answer1)
answer2 = searching_number_or_position (Li_st, y)
print(answer2)
answer3 = searching_number_or_position (Li_st, z)
print(answer3)

#4

from math import sqrt

class Class_Coordinates:
  @classmethod
  def arg_length(cls,arg1, arg2):
    try:
      r = (sqrt(arg1**2 + arg2**2))
      return r
    except TypeError: print('Please, enter a valid data. x and y values have to be numbers type.')

  
  
print(Class_Coordinates.arg_length(9,-5.22))
print(Class_Coordinates.arg_length('e',7))

#5 task with unittest

def square(arg_a,arg_b):
    try:
      if type(arg_a) == int or type(arg_a) == float and type(arg_b) == int or type(arg_b) == float:
        if arg_a>0 and arg_b>0:
          total = arg_a * arg_b
          return total
        else: raise TypeError('Every argument have to be positive number > 0')
      raise TypeError('Every argument have to be number')
    except: return 

if __name__ == '__main__':
  a = 4
  b = 3
  solution = square(a,b)
  print(solution)
  