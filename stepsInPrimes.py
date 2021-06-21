'''
The prime numbers are not regularly spaced. For example from 2 to 3 the step is 1. From 3 to 5 the step is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs of 2-steps primes:

3, 5 - 5, 7, - 11, 13, - 17, 19, - 29, 31, - 41, 43

We will write a function step with parameters:

g (integer >= 2) which indicates the step we are looking for,

m (integer >= 2) which gives the start of the search (m inclusive),

n (integer >= m) which gives the end of the search (n inclusive)

In the example above step(2, 2, 50) will return [3, 5] which is the first pair between 2 and 50 with a 2-steps.

So this function should return the first pair of the two prime numbers spaced with a step of g between the limits m, n if these g-steps prime numbers exist otherwise nil or null or None or Nothing or [] or "0, 0" or {0, 0} or 0 0(depending on the language).

Examples:
step(2, 5, 7) --> [5, 7] or (5, 7) or {5, 7} or "5 7"
'''
'''
import time


def step(g, m, n):
    
    primes = []

    for num in range(m,n):
        if all(num % i !=0 for i in range(2,num)):
            primes.append(num)
    
    first = 0
    last = 0
                
    for each in primes:
        if each + g in primes:
            first = each
            last = (each + g)
            break

    if first == 0:
        return None
    
    print([first, last])
    return [first, last]


t0 = time.time()
step(10,300000,400000)
t1 = time.time()

print(t1 - t0)
'''


def is_prime(min, max):
    list_a = list(range(min, (max+1)))
    
    prime_numbers = []
    
    for each in list_a:
        if each > 1:
            for i in range(2, each):
                if (each % i) == 0:
                    break
            else:
                prime_numbers.append(each)
    
    return prime_numbers


def step(g, m, n):

    primes = is_prime(m ,n)
    
    print(primes)
    
    first = 0
    last = 0
                
    for each in primes:
        if each + g in primes:
            first = each
            last = (each + g)
            break

    if first == 0:
        return None
    
    print([first, last])
    return [first, last]

step(10,300,400)




