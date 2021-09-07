def sumofdigits(n):
	assert n >= 0 and int(n) == n , "input should be positive integer"
	if n == 0:
		return 0
	else:
		return n%10 + sumofdigits(int(n/10))

if __name__ == '__main__':
	print (sumofdigits(4))
	print (sumofdigits(89767))
	try:
		print (sumofdigits(-1))
	except AssertionError as e:
		print (e)
	
	try:
		print (sumofdigits(7.9))
	except AssertionError as e:
		print (e)

	print (sumofdigits(9878)) 