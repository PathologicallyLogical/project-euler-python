
f = open("input.txt", "r")


def line_read(string):
	a = string.split()
	fin = []
	for num in a:
		fin.append(int(num))
	return fin

def file_read(the_file):
	final = []
	for word in the_file:
		final.append(line_read(word))
	return final

a = file_read(f)
#print a
def producter(arr, i):
	count = 1
	for j in range(i, i+4):
		count *= arr[j]
	return count

def horizontal(matrix):
	greatest = 0
	for arr in matrix:
		for i in range(len(arr) - 3):
			temp = producter(arr, i)
			if temp > greatest:
				greatest = temp
	return str(greatest)

def vertical(matrix):
	return horizontal([list(i) for i in zip(*matrix)])

def zero_adder_right(matrix):
	new = []
	l = len(matrix)
	for i in range(0, l):
		new.append(([0]*i) + (matrix[i]) + ([0]*(len(matrix) - i)))
	return new

def zero_adder_left(matrix):
	n = []
	l = len(matrix)
	for i in range(0, l):
		n.append(([0]*(len(matrix) - i)) + (matrix[i]) + ([0]*i))
	return n

def diagonal(matrix):
	left = vertical(zero_adder_left(matrix))
	right = vertical(zero_adder_right(matrix))
	if int(left) > int(right):
		return left
	return right

def compare(matrix):
	b = int(horizontal(matrix))
	c = int(vertical(matrix))
	d = int(diagonal(matrix))
	return max([b,c,d])


print compare(a)
f.close()