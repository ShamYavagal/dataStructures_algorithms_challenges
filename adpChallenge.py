# Write a Function that takes a string as an Input and return True if that string can be a palindrome with string manupilation/shifting and False if it cannot  

#Example

# aabbccdd is not a palindrome but with string manipulation it can be. abcddcba


#my solution

count = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,0:0}

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,0]

def canBePalindrome(string1):
    for each in string1:
        if each in chars: 
            count[each] += 1
            
    odd_count = 0
    for key, value in count.items():
        if value % 2 != 0:
            odd_count += 1
    
    if odd_count > 1:
        return False
    return True
    
print(canBePalindrome('abcddcba123ab'))


