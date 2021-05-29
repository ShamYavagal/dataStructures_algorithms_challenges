'''
Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)
'''

def find(n):
    
    totalSum = []
    for each in range(1,(n+1)):
        if each % 3 == 0:
            totalSum.append(each)
        elif each % 5 == 0:
            totalSum.append(each)
    return sum(totalSum)

