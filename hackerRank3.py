'''
def repeatedString(s, n):
    initial = s
    num = 0
    for each in range(n-1):
        s = s+initial
    new_s = s[:n]
    for each in new_s:
        if each == 'a':
            num +=1
    print(num)
    return num
       
print(repeatedString('a', 1000000000000))
'''
'''
def repeatedString(s, n):
    if len(s) == 1 and s != 'a':
        return 0
    if len(s) == 1:
        return n
    num = 0
    s = s * n
    new_s = s[:n]
    for each in new_s:
        if each == 'a':
            num +=1
    print(num)
    return num

print(repeatedString('x', 1000000000000))
'''
'''
def repeatedString(s, n):
    if len(s) == 1 and s != 'a':
        return 0
    if len(s) == 1:
        return n
    all_a = []
    for each in s:
        if each != 'a':
            all_a.append("false")
        else:
            all_a.append("true")
    if "false" not in all_a:
        return n
    num = 0
    while len(s) <= n:
        s += s
    new_s = s[:n]
    for each in new_s:
        if each == 'a':
            num +=1
    print(num)
    return num

print(repeatedString('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 534802106762))
'''

'''
def repeatedString(s, n):
    if len(s) == 1 and s != 'a':
        print(n)
        return 0
    if len(s) == 1:
        print(n)
        return n
    all_a = []
    for each in s:
        if each != 'a':
            all_a.append("false")
        else:
            all_a.append("true")
    if "false" not in all_a:
        print(n)
        return n
    num_As = 0
    for each in s:
        if each == 'a':
            num_As +=1
    if float((n / len(s))).is_integer():
        total_As = (n / len(s)) * num_As
        print(int(total_As))
    else:
        val = n / len(s)
        major = int(str(val).split('.')[0])
        remainder = int(str(val).split('.')[1][0])
        extras = s[:remainder]
        extra_As = 0
        for each in extras:
            if each == 'a':
                extra_As +=1
        total_As = (major * num_As)
        total_As = total_As + extra_As
    print(int(total_As))
'''

def repeatedString(s, n):
    if len(s) == 1 and s != 'a':
        print(0)
        return 0
    if len(s) == 1:
        print(n)
        return n
    all_a = []
    for each in s:
        if each != 'a':
            all_a.append("false")
        else:
            all_a.append("true")
    if "false" not in all_a:
        print(n)
        return n
    num_As = 0
    for each in s:
        if each == 'a':
            num_As +=1
    if float((n / len(s))).is_integer():
        total_As = (n / len(s)) * num_As
        print(int(total_As))
    else:
        val = n / len(s)
        major = int(str(val).split('.')[0])
        remainder = n % len(s)
        extras = s[:remainder]
        extra_As = 0
        for each in extras:
            if each == 'a':
                extra_As +=1
        total_As = (major * num_As)
        total_As = total_As + extra_As
        print(int(total_As))
      
     
#print(repeatedString('aba', 10))
print(repeatedString('kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm', 736778906400))
