#First task

f = open('text_green.txt', 'w')
f.write('green color is the color of spring !\ngreen grass gives special mood in spring\nthis string for task2 test')
f.close



f = open('text_green.txt', 'r')
text1 = f.read()

f1 = open('text_rad.txt', 'w')
text2 = text1.replace('green', 'rad')
f1.write(text2)

f1.close()
f.close()

#Second task

f = open('text_green.txt', 'r')
lines = f.readlines()


f2 = open('text_none.txt', 'w')


#f2.seek(0)
#for i in lines:
    #if i != "green":
        #f2.write(i)

for line in lines: 
    if 'green' in line:
        f.readline()
    else:
    	f2.write(line)

f2.close()
f.close()

#Third task

#Creating new file (should be performed 1 time), after manual changing one of the files should be commented to be shure that function of compare works correctly
f3 = open('text_text.txt', 'w')
f3.write(text1)
f3.close()


f = open('text_green.txt', 'r')
text1 = f.read()
f3 = open('text_text.txt')
text3 = f3.read()

if text1 == text3:
	print ('True')
else:
	print ('False')






