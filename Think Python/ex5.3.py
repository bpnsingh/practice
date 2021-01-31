def is_triangle(a,b,c):
	if a>b+c or b>a+c or c>a+b:
		print ("No")
	else:
		print ("yes")

if __name__ == '__main__':
	a,b,c= map (int,input("Enter sides of triangles:").split())
	is_triangle(a,b,c)
