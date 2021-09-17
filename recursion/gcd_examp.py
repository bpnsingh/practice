'''
gcd(48,18)
1st = 48/18   2   12
2nd = 18/12   1   6
3rd = 12/6    2   0
euclidian algo
gcd (a,0) = a
gcd(a,b) = gcd (b,a mod b)

'''

def gcd (a,b):
    assert int(a) == a and int(b) == b , "Input should be integer"
    if a <1:
        a*=-1
    if b<1:
        b*=-1
    if b==0:
        return a
    else:
        return   gcd(b,a%b)


if __name__ == '__main__':
    print(gcd(48,18))
    print(gcd(48, -18))
    print(gcd(48, 18.8))