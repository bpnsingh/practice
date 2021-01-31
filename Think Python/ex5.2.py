def check_fermet(a,b,c,n):
	lhs = a**n+b**n
	rhs = c ** n
	if n > 2 and (lhs == rhs):
		print ("Holy smoke !! Fermet was wrong")
	else:
		print ("No That doesn't work")

if __name__ == '__main__':
	check_fermet(1,1,1,5)
	check_fermet(10,8,67,5)

