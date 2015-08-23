def add_5_and_3_factors(length):
	count = 0
	for i in range(length): 
		if i%5==0 or i%3==0:
			count+=i
	return count

def fizz_buzz(num):
	for i in range(1,num):
		if i%3 == 0 and i%5 == 0:
			print "Fizzbuzz!"
		elif i%3 == 0:
			print "Fizz"
		elif i%5 == 0:
			print "Buzz"
		else:
			print i
euler1(10)
fizz_buzz(100)
#adds all the factors of 5 and 3 together up to a certain number.
#bonus fizzbuzz
#completed August 2015
#contributions by kennypybot Aug. 22, 2015
