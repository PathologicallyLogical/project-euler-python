
def palindrome(num):
	numlist = []
	storage = num
	while num> 0:
		digit = num%10
		numlist.append(digit)
		num = int(num/10)
	final = ""
	for i in numlist:
		temp = str(i)
		final +=temp
	finalint = int(final)
	if storage == finalint:
		return True
	else:
		return False
def three_digit_check():
	results = []
	for x in range(101,999):
		for y in range(101,999):
			z = x*y
			if palindrome(z):
				results.append(z)
	print max(results)
three_digit_check()

#started/completed August 2015
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
