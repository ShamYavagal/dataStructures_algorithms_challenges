def sock(n, arr):
    total = 0
    dict1 = {}
    for index, value in enumerate(arr):
        dict1[value] = 0 if not dict1.get(value) else dict1[value]
        dict1[value] +=1
    print(dict1)
    for key, val in dict1.items():
        if val % 2 == 0:
            dict1[key] = val / 2
        else:
            dict1[key] = (val - 1) / 2
        total += dict1[key]
    return int(total)

sock(10, [1,2,3,4,5,6,6,40,3,3,3,3,10,1])

#-------------------------------------------------------------------------------------------