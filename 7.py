def isPrime(x):
    for i in range(2,int(x**.5)+1):
        if x%i == 0:
            return False
    return True
    
primelist = 1
x = 3
while primelist <10001:
    if isPrime(x):
        primelist+=1
    x+=2
print x-2


#started August 22, 2015
#completed August 22, 2015
#not very efficient. Fix later.

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
