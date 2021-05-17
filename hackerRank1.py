def jumpingOnClouds(c):
    if len(c) % 2 == 0:
        arrlen = len(c)
    else:
        arrlen = len(c) - 1
            
    if 1 not in c:
        jumps = arrlen / 2
        print("RETURNING HERE - 1")
        return int(jumps)
        
    even = []
    odd = []
    for index, value in enumerate(c):
        if index % 2 == 0 and value == 0:
            even.append(True)
        elif index % 2 == 0 and value == 1:
            odd.append(True)
    print(odd)
            
    if True not in odd:
        jumps = arrlen / 2
        print("RETURNING HERE - 2")
        if c[-1] == 1:
            return int(jumps - 1)
        return int(jumps)
    
    position = 0
    pos_list = []
    for index, value in enumerate(c):
        if position <= (len(c) - 3):
            if c[position + 2] == 0:
                position += 2
                pos_list.append(position)
            elif c[position + 1] == 0:
                position += 1
                pos_list.append(position)
        elif position <= (len(c) - 2):
            if c[position + 1] == 0:
                 position += 1
                 pos_list.append(position)
        if position >= len(c):
            break
        if index == (len(c) -1):
            break
                
    print(pos_list)
    return len(pos_list)


jumpingOnClouds([0,0,1,0,1,0,0,1,0,0,1,0,0,0,1])

            
            