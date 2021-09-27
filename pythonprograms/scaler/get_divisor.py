'''
If input is 60, try to get all possible unique divisor.
60 --> 1,2,3,4,5,6,10,12,15,30,60
'''
import math

def get_divisor(N):
    assert N > 0 and int(N)==N, "input should be positive integer"
    i=1
    counter = int(math.sqrt(N))
    while i < counter:
        if N % i == 0:
            print("{0},{1}".format(i,int(N/i)))
        i+=1
    if N//i ==i:
        print (i)




if __name__ == '__main__':
    #get_divisor(60)
    #print()
    get_divisor(9)