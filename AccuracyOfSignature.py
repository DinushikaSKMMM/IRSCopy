import math
from decimal import Decimal
import sklearn
from sklearn.metrics import accuracy_score
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# array1 =[22227,1390.704748,2.77777778,0.38588542,36826,0.60356813,168.2269163,85.36746979,57600,400,144]
# array2 = [22353,1444.645872,2.95138889,0.3652451,37888.5,0.58996793,168.7030632,86.29348755,61200,425,144]


array1 = [7781.5,7781.5,2.31896552,0.24937508,19907.5,0.39088283,	9.53749805,92.08638763,269,269]
array2 = [25125,25125,1.765625,0.38601586,44873,0.55991353,178.8578865,91.23092651,339,339]
arrayNew = []
multiArray= []
sum = 0
for a1,a2 in zip(array1, array2):
    accuracy = a1 - a2
    multi = accuracy*accuracy
    sum += multi
    arrayNew.append(accuracy)
    multiArray.append(multi)
    #multi.append(multiArray)
    #arrayNew.append(accuracy)
# print(arrayNew)
featuersMultification = multi
# print(multiArray)
m1=np.mean(array1)
m2=np.mean(array2)
# print(np.mean(array1))
# print(np.mean(array2))
# print("sqrot")
# print(format(math.sqrt((m1-m2)*(m1-m2)), '.6f'))
# print(format(m1))
sq1=format(math.sqrt((m1-m2)*(m1-m2)))
m1 =format(m1,'.6f')
dive = float(sq1)/float(m1)
# print("dive")
# print(format(dive,'.7f'))
#print(format(((math.sqrt((m1-m2)*(m1-m2)))//m1),'.6f'))
# print((dive)*100)
accuracy = ((1.0 - dive)* 100)
print("Accuracy")
print(accuracy)
# print(math.sqrt(4))

# print("acccvvvvvvvv")
# acc = accuracy_score([array1],[array2])
# accuracy_score(array1, array2)
#print(accuracy_score(array1, array2))
# accuracy_score(array1, array2, normalize=False)
# print(accuracy_score(array1, array2, normalize=False))
# print(acc)


# weights = [8, 9, 1, 3, 4, 4, 7, 5, 6, 6,5]
# a = []
# a = [i * j for i, j in zip(multiArray,weights)]
# print(a)
# total = 0.00
# for i in a:
#     total +=i
#
# print(total)
# print(math.sqrt(total))
