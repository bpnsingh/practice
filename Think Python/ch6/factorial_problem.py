'''
Calculate  factorial
'''

def fact (n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)
if __name__ == '__main__':
	numbers = list(map(int,input("Enter number of which factorial>").split()))
	for n in numbers:
		print (f'dactorial of {n} is {fact(n)}\n')