def fizzbuzz():
	for i in range(1,101):
		msg=""
		if i % 3 == 0:
			msg+='fizz'
		if i% 5  == 0:
			msg+='buzz'
		if msg == "":
			print (i)
		else:
			print (msg)

def fizzbuzz_without_mod():
	c3 = 0
	c5 = 0
	for i in range(1,101):
		msg=""
		c3+=1
		c5+=1
		#print (c3,c5)
		if c3 == 3:
			msg+='fizz'
			c3=0
		if c5 == 5:
			msg += 'buzz'
			c5 = 0
		if msg == "":
			print (i)
		else:
			print(msg)





if __name__ == '__main__':
	#fizzbuzz()
	fizzbuzz_without_mod()

