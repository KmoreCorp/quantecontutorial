## Exercise 1
# part 1
x = [3,4,5]
y = [1,5,9]

z = zip(x,y)
pd = list (x * y for x,y in z)

print(pd)


# part 2
a = sum(x % 2 == 0 for x in range(100))
print(a)


# part 3
pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
count = sum(x % 2==0 and y % 2 == 0 for x, y in pairs)
print(count)

## Exercise 2
def p(x,coeff):
	sum = 0
	for n in range(len(coeff)):
		sum += coeff[n] * x**n
	return sum

ls = [3,7,5]
print(p(2,ls))

## Exercise 3
def upcase(data):
	ls = data.split()
	count = 0
	for word in ls:
		if word[0]== word[0].upper() and word[0].isalpha():
			count += 1
		else:
			pass
	return count

data = 'Span, German are countries'
print(upcase(data))


## Exercise 5
def f(x, n, interval):
	length = interval[1]-interval[0]
	piece = length / (n-1)
	index = (x-interval[0]) // piece
	approx_0 = interval[0] + index * piece
	approx_1 = approx_0 + piece
	approx = (approx_0 + approx_1) / 2

	return approx

