'''
Given a number A, check if it is a magic number or not.
A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1, then the number is a magic number.
'''

def check_magic(N):
    if N < 10:
        return N
    else:
        sum= (N % 10 + check_magic(N // 10))
        if sum > 10:
            check_magic(sum)
        else:
            if sum == 1:
                return 1
            else:
                return 0




if __name__ == '__main__':
    print (check_magic(83557))
    print(check_magic(1291))

