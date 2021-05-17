def sumnum(num):
    list1 = []
    for i in range(1,num):
        if i % 3 == 0 or i % 5 == 0:
            if i < 1000:
                list1.append(i)
    print(list1)
    return sum(list1)

sumnum(1000)

###############################################################################

def genfib(n):
    list2 = []
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
        if a % 2 == 0 and a <= 4000000:
            list2.append(a)
    print(list2)
    print(sum(list2))

genfib(200)

###############################################################################

l1 = []
for i in range(100,1000):
    for j in range(100,1000):
        result = str(i*j)
        if len(result) == 5:
            key1 = ''.join(result[0:2])
            value1 = ''.join(result[3:5])
            if key1 == value1[::-1]:
                l1.append(int(result))
        if len(result) == 6:
            key2 = ''.join(result[0:3])
            value2 = ''.join(result[3:6])
            if key2 == value2[::-1]:
                l1.append(int(result))

sorted(l1)[-1]

###############################################################################












    