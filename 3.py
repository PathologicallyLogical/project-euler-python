
def factor(x):
	factors = []
	z=math.sqrt(x)
	zy = int(z)
	for k in range(1,zy):
		if x%k==0:
			factors.append(k)
	print "The factors of "+str(x)+" are",factors
	return factors
	#works correctly. returns primes
def primes(x):      
	original = factor(x)
	print "original", original
	#saves the factors of x
	i=0
	while (i < len(original)):
		print "i:",original[i] 
		#loop through the factor list
		temp = factor(original[i])
		#find the factors of each factor
		for j in range(len(temp)):
			#loop through the factors of each factor
			if temp[j] > 1:
				print "Now removing i:",original[i], ", cuz j:",temp[j]
				original.remove(original[i])
				i=i-1
				break
			#remove any factors that aren't prime
		i = i + 1
	print "This is the list of primes: "+str(original)
		return original
	final = primes(x)
	print final[len(final)-1]
	return final[len(final)-1]

#started/completed August 2015	
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
