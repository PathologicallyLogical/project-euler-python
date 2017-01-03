from math import *
def divisor_finder(n):
	count = 0
	for i in range(1,int(sqrt(n)+1)):
		if n % i == 0:
			count += 2
	if n % int(sqrt(n)) == 0:
		count -= 1
	return count

def triangle_gen(n):
	stop = 1
	while n >= stop:
		yield sum(range(stop+1))
		stop += 1

def marginally_better():
	tri = triangle_gen(5000000)
	for i in tri:
		if divisor_finder(i) > 499:
			return i

print divisor_finder(76576500)
