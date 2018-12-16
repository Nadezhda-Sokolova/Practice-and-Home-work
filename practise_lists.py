#Lists and list comprehensions
#First task
exec1 = [123, 'practise', 2.345, 'test', 'examples', 345, 678, 0.456]
exec1.reverse()
print (exec1)

#Scond task
list1 = ['one', 'two', 'oneandtwo', 'three', 'none', 'four']
exec2 = list1[:]
print (exec2)
exec3 = list1[1:]
print (exec3)

#Third task
S = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exec4 = [S[i] for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if i % 2 == 0]
print (exec4)

#Forth task
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
exec5 = [L[i] for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] if i % 3 == 0]
print (exec5)

#Fifth task
S = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exec6 = [i * 10 for i in exec4]
print (exec6)
