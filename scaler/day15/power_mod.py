'''
Given A,n,P fing a^n % P
'''

def powermod(a,n,p):
    power = 1
    for i in range(n):
        power = (power * (a % p))%p
    return power

if __name__ == '__main__':
    print (powermod(2,10,3))