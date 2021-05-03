def check_fermet(a,b,c,n):
	lhs = a**n+b**n
	rhs = c ** n
	if n > 2 and (lhs == rhs):
		print ("Holy smoke !! Fermet was wrong")
	else:
		print ("No That doesn't work")

if __name__ == '__main__':
	a,b,c,n = map(int,input("ENter Numbers:>").split())
	check_fermet(a,b,c,n)
	a,b,c,n = map(int,input("ENter Numbers:>").split())
	check_fermet(a,b,c,n)