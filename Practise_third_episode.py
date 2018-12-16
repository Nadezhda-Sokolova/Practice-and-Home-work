#Students and their academic performance

name = ['Alexander', 'Mihail', 'Elena', 'Svetlana']
subject = ['mathematics', 'geometry', 'russuan_language', 'literature']
Alexander = [5, 5, 4, 4]
Mihail = [4, 4, 3, 3]
Elena = [4, 4, 5, 5]
Svetlana = [5, 5, 5, 5]

#First method: special case

#1 Middle rating for each student
mid_A = float(sum(Alexander))/float(len(Alexander))
mid_M = float(sum(Mihail))/float(len(Mihail))
mid_E = float(sum(Elena))/float(len(Elena))
mid_S = float(sum(Svetlana))/float(len(Svetlana))
Middle = [mid_A, mid_M, mid_E, mid_S]
dictMiddle = dict(zip(name,Middle))
print(dictMiddle)

#2 Middle value for each subject

M = [[5, 5, 4, 4],
     [4, 4, 3, 3],
     [4, 4, 5, 5],
     [5, 5, 5, 5]]

mathematics = [row[0] for row in M]
mid_mathematics = float(sum(mathematics))/float(len(name))

geometry = [row[1] for row in M]
mid_geometry = float(sum(geometry))/float(len(name))

russuan_language = [row[2] for row in M]
mid_rl = float(sum(russuan_language))/float(len(name))

literature = [row[3] for row in M]
mid_literature = float(sum(literature))/float(len(name))

mid_subject = [mid_mathematics, mid_geometry, mid_rl, mid_literature ]
dictSubject = dict(zip(subject, mid_subject))
print(dictSubject)

#3 Students with the best academic performance

best_student = max(dictMiddle, key = dictMiddle.get)
print(best_student)


# 4 Students with the worst academic performance


worst_student = min(dictMiddle, key=dictMiddle.get)
print(worst_student)

#Second method: common case

Alexander = [5, 5, 4, 4]
Mihail = [4, 4, 3, 3]
Elena = [4, 4, 5, 5]
Svetlana = [5, 5, 5, 5]
name = [Alexander, Mihail, Elena, Svetlana]
subject = ['mathematics', 'geometry', 'russuan_language', 'literature']
name1 = ['Alexander', 'Mihail', 'Elena', 'Svetlana']




#1 Middle rating for each student
dict = {}
i = 0

while i < len(name):
 middle_assesment = float(sum(name[i]))/float(len(name))
 print(middle_assesment)
 dict[name1[i]] = middle_assesment
 i+=1

print(dict)

#2 Middle value for each subject
dict_sub = {}
j = 0
while j<len(subject):
 #mid_subject = [row[j] for row in name]
 mid_subject = float(sum([row[j] for row in name]))/float(len(subject))
 dict_sub[subject[j]] = mid_subject
 j+=1

print(dict_sub)


#3 Students with the best academic performance

best_student = max(dict, key = dict.get)
print(best_student)


# 4 Students with the worst academic performance


worst_student = min(dict, key=dict.get)
print(worst_student)

