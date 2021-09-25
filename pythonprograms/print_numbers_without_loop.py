

def print_number(n):
	if n <= 100:
		print (n)
		n+=1
		print_number(n)	

if __name__ == '__main__':
	print_number(1)