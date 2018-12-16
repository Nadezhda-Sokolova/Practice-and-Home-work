# First excercise
a = 2
b = 3
a1 = str (a)
b1 = str (b)
c = a1 + b1
print (c)

d = int (a1 + b1)
print (d)

d1 = a + b
print (str(d1))

c1 = c * 2
print (c1)

# Second exercise
line = 'ABCDCDC'
sub = 'CDC'
n = line.count(sub)
print (n)

import re
print (len (re.findall('(?=CDC)', line)))


#Third exercise

text = 'It was the best of times it was the worst of times it was the age of wisdom it was the age of foolishness'
text = text.lower()
#print (text)
list_of_text = text.split(' ')
#print (list_of_text)
dictionary = dict()
for word in list_of_text:

  if dictionary.get(word) == None:
    dictionary[word] = 1
  else: 
    dictionary[word] += 1

print (dictionary)

print (dictionary['IT'.lower()])






#print (help (str))
