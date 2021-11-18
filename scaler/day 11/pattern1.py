'''
rows = 3
for row in range(1, rows+1):
    for column in range(1, rows + 1):
        if column <= row:
            print(column, end=' ')
        else:
            print(0, end=' ')

    print("")
'''
A=3
for i in range(1,A+1):
   for space in range(i,A):
       print(end="  ")
   for j in range(i,0,-1):
       print(j,end=" ")
   print()
