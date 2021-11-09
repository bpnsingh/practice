import math

def check_prime_bool(N):
    if N<2:
        #To handle negative and 1
        return False
    i=2
    loop_limit= int(math.sqrt(N))
    while (i*i <= N):   
        if N%i == 0:
            return False
        i+=1
    return True

if __name__ == "__main__":
    print (check_prime_bool(1))
    print(check_prime_bool(2))
    print(check_prime_bool(5))
    print(check_prime_bool(50))
    print(check_prime_bool(9))
    print(check_prime_bool(16))
