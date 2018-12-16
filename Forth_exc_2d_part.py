# Second task
# All posible combinations of letters in string without itertools


def combinations(line):
    if len(line) == 0:
        return ['']
    prevList = combinations(line[1:len(line)])
    nextList = []
    for i in range(0,len(prevList)):
        for j in range(0,len(line)):
            newString = prevList[i][0:j]+line[0]+prevList[i][j:len(line)-1]
            if newString not in nextList:
                nextList.append(newString)
    return nextList

line = 'abc'

L1 = list(combinations(line))
print(L1)

# =====================================================

#Third task

sentence = 'yes and no'
sentence = sentence.split()
#print(sentence)

import itertools
from itertools import permutations
k = list(itertools.permutations(sentence,len(sentence)))
#print(k)

k = [(' '.join(i)) for i in k]
print(k)



