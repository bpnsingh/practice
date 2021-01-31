
def fib(n):
    value = 1
    if n in fib_cache:
        return fib_cache[n]
    if n == 1 or n == 2:
        value = 1
    elif n>2 :
        value = fib(n-1) + fib(n-2)
    fib_cache[n] = value
    return value

if __name__ == "__main__":
    fib_cache = {}
    for i in range(100):
        print (i,"-->",fib(i))