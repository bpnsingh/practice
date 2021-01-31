def fact(n):
    if n==0:
        return 1
    else:
        return  n * fact(n-1)

def fact_loop(n):
    result=1
    while (n > 1):
        result = result * n
        n -= 1
    return result

cache={}
def fact_cache(n):
    if n in cache:
        return cache[n]
    if n==0:
        value = 1
    else:
        value  = n * fact(n-1)

    cache[n]=value
    return value

if __name__ == '__main__':
    #print ("5!-->",fact(100))
    #print("5!-->", fact_loop(100))
    #print("5!-->", fact_cache(100))
    #for n in range(100):
    #    print (n,"-->",fact_cache(n))
    for n in range(200):
        print (n,"-->",fact(n))