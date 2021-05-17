#def getShortestUniqueSubstring(arr, str):
 
array =  ["x","y","z"]
string = "xyyzyzyx"

string = [s for s in string]

dict1 = {}


'''
for a in array:
    for b, value in enumerate(string):
        print(b)
        if value == a:
            dict1.setdefault(a, []).append(b)
            break
            #dict1.setdefault('A', []).append(b)
'''

'''
for a, val in enumerate(string):
    for b, value in enumerate(array):
        print(b)
        if value == val:
            dict1.setdefault(value, []).append(a)
            #dict1.setdefault('A', []).append(b)    
'''


for a in array:
    for b, value in enumerate(string):
        if value == a:
            dict1.setdefault(a, []).append(b)

#print(dict1)
        
list1 = []
list2 = []
 
for key, value in dict1.items():
    list1.append(sorted(value)[0])
    list2.append(sorted(value)[-1])

list1 = sorted(list1)
list2 = sorted(list2)

#print(list1, list2)

list1_first = list1[0]
list2_first = list2[0]

list1_last = list1[-1]
list2_last = list2[-1]

list1_last = list1_last+1
list2_last = list2_last+1

#print(list1_last)
#print(list2_last)

string_len1 = len(string[list1_first:list1_last])

string_len2 = len(string[list2_first:list2_last])

#print(string_len1, string_len2)

#print(string_len1) if string_len1 < string_len2 else print(string_len2)

if string_len1 < string_len2:
    print(''.join(string[list1_first:list1_last]))
elif string_len1 > string_len2:
    print(''.join(string[list2_first:list2_last]))
elif string_len1 == string_len2:
    print(''.join(string[list1_first:list1_last]))