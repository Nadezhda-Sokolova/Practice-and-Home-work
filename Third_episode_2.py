#Second task 

i = 0 #this year
tree_high = 1

while tree_high < 100:
 i += 1
 #print(i)
 tree_high = (tree_high * 2) + 1
 #print(tree_high)
print(i)

#====================
#Third task

S0 = 40
V1 = 80
V2 = 60

S2 = S0*V2/(V1-V2)
t = S2 / V2
print ('Distance from B to C is', S2)
print ('Time to meet is', t)

