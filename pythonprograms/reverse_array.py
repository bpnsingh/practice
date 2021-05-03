def reverese_array(input_list):
	count = len(input_list)
	reversed_list = []
	while count > 0:
		reversed_list.append(input_list[count])
		count = count -1
	print (reversed_list)


if __name__ == '__main__':
	reverese_array([1,2,3,4,5])

