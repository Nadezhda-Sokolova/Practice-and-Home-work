#Strings
#First task
S = 'Tetsing'
S1 = S [::-1]
print (S1)

#Second task
S2 = 'Anfiska\tis\tname\tof\tmy\tcat'
print(S2)
S2.split('\t') 
#print (S2)
S3 = S2.split('\t')[::-1]
#print (S3)
S4 = '\t'.join(S3)
print (S4)

#Third task
S5 = 'Alice and Bob love each other'
S6 = 'Dick and Jane hate each other'
S7 = '{0}, {1}'.format(S5, S6)
print (S7)








