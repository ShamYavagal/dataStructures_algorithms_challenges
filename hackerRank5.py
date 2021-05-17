A = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]
#B = [[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]]

B = A

print( '\n'.join( [''.join ( ['{:4}'.format(item) for item in row] ) for row in A] ) )

'''
   1   2   3   4   5   6
   7   8   9  10  11  12
  13  14  15  16  17  18
  19  20  21  22  23  24
  25  26  27  28  29  30
  31  32  33  34  35  36
'''


'''
list1 = []
sublist = []

for index, each in enumerate(A):
    if index <= 2:
        for i, j in enumerate(each):
            if i <= 2:
                sublist.append(each[i])

list1.append(sublist)              
sublist = []

for index, each in enumerate(A):
    if index <= 2:
        for i, j in enumerate(each):
            if i >= 3:
                sublist.append(each[i])
                
list1.append(sublist)              
sublist = []
'''

list1 = []
sublist = []

'''
while len(A[0]) >= 3:
    for index, each in enumerate(A):
        sublist.append(each[0])
        sublist.append(each[1])
        sublist.append(each[2])
        each.pop(0)


while len(sublist) >= 9:
    #for i, j in enumerate(sublist):
    list1.append(sublist[:9])
    sublist = sublist[3:]
    #print(sublist)
'''

#print(sublist)
#print(list1)

dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}

'''
for each in range(1,5):
    if len(A[5]) >= 3:
        dict1.setdefault(each, []).append(A[0][:3])
        dict1.setdefault(each, []).append(A[1][:3])
        dict1.setdefault(each, []).append(A[2][:3])
        A[0].pop(0)
        A[1].pop(0)
        A[2].pop(0)
        
for each in range(5,9):
    if len(A[5]) >= 3:
        dict2.setdefault(each, []).append(A[3][:3])
        dict2.setdefault(each, []).append(A[4][:3])
        dict2.setdefault(each, []).append(A[5][:3])
        A[3].pop(0)
        A[4].pop(0)
        A[5].pop(0)
''' 


for index, each in enumerate(range(1,5)):
    if len(A[5]) >= 3:
        dict1.setdefault(each, []).append(A[0][index:index+3])
        dict1.setdefault(each, []).append(A[1][index:index+3])
        dict1.setdefault(each, []).append(A[2][index:index+3])
        
for index, each in enumerate(range(5,9)):
    if len(A[5]) >= 3:
        dict2.setdefault(each, []).append(A[3][index:index+3])
        dict2.setdefault(each, []).append(A[4][index:index+3])
        dict2.setdefault(each, []).append(A[5][index:index+3])


for index, each in enumerate(range(9,13)):
    if len(B[5]) >= 3:
        dict3.setdefault(each, []).append(B[1][index:index+3])
        dict3.setdefault(each, []).append(B[2][index:index+3])
        dict3.setdefault(each, []).append(B[3][index:index+3])


for index, each in enumerate(range(13,17)):
    if len(B[5]) >= 3:
        dict4.setdefault(each, []).append(B[2][index:index+3])
        dict4.setdefault(each, []).append(B[3][index:index+3])
        dict4.setdefault(each, []).append(B[4][index:index+3])


#print(dict1)
#print(dict2) 
#print(dict3)
#print(dict4)

flist = [] # final list
clist = [] # concat list
numlist = [] # number list
sumlist = []

for key,value in dict1.items():
    flist.append(value)
for key,value in dict2.items():
    flist.append(value)
for key,value in dict3.items():
    flist.append(value)
for key,value in dict4.items():
    flist.append(value)

for each in flist:
    clist.append(each[0] + each[1] + each[2])
    
    
    
for each in clist:
    templist = []
    for index, item in enumerate(each):
        if index != 3 and index != 5: 
            templist.append(item)
    numlist.append(templist)
    

for each in numlist:
    sumlist.append(sum(each))

print(sorted(sumlist)[-1])
        
#print(flist)
#print(clist)
#print(numlist)
#print(sumlist)