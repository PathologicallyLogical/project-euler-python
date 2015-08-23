def sumOfSquares(x):
    count = 0
    for i in range(x+1):
        count += i**2
    return count
def squareOfSums(y):
    c = 0
    for i in range(y+1):
        c += i
    return c**2
def final(z):
    return squareOfSums(z)-sumOfSquares(z)
    
final(100)

#started August 22, 2015
#completed August 22, 2015
"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
