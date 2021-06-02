# Given an array of integers greater than zero, find if there is a way to
# split the array in two (without reordering any elements) such that the
# numbers before the split add up to the numbers after the split. If so,
# print the two resulting arrays.
#
#In [1]: can_partition([5, 2, 3])  
#([5], [2, 3])
#Out[1]: True
#
#In [2]: can_partition([2, 3, 2, 1, 1, 1, 2, 1, 1])
#([2, 3, 2], [1, 1, 1, 2, 1, 1])
#Out[2]: True
#
#In [3]: can_partition([1, 1, 3])
#Out[3]: False


def can_part(arr1):
    if len(arr1) == 1:
        return False
    
    k = 0
    while k < (len(arr1) - 1):
        for i,j in enumerate(arr1,1):
            k += 1
            if sum(arr1[:i]) == sum(arr1[i:]):
                return True 
    return False
           
           
print(can_part([3,1,5,6,3]))