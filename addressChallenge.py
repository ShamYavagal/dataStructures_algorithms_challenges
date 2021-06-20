'''
You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. 
Naturally, you would like to find out the house number of the people on the other side of the street. The street looks something like this:

Street
 1|   |12   # Take 10 for example, Create a list of range from 1,10 (1..9) find the index of 9 in the list, then reverse the list and fetch the index of the reversed list.
 3|   |10
 5|   |8  
 7|   |6
 9|   |4
11|   |2

Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps. When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.

Example: Given your house number address and length of street n, give the house number on the opposite side of the street.

over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
'''

def over_the_road(address, n):
    n = n * 2
    left = []
    right = []
    index_num = 0
    opp_value = 0
    for each in range(1,(n+1)):
        if each % 2 == 0:
            right.append(each)
        else:
            left.append(each)
            
    left.reverse()
    
    if address % 2 == 0:
        for index, value in enumerate(right):
            if address == value:
                index_num = index
                break
        opp_value = left[int(index_num)]
                
    else:
        for index, value in enumerate(left):
            if address == value:
                index_num = index
                break
        opp_value = right[int(index_num)]

    print(opp_value)
    return(opp_value)
