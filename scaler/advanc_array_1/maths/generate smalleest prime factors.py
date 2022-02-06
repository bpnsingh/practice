'''
N = 10
2,3,2,5,2,7,2,3,2
'''
def smallest_prime_factor(N):
    #create an answer array
    ans = []
    for i in range(N+1):
        if i>1:
            ans.append(i)
        else:
            ans.append(None)

    i = 2
    while i <= N:
        if i == ans[i]:
            j = i * i
            while j <= N:
                ans[j] = min(i,ans[j])
                j+=i
        i+=1
    for i in range(2,N+1):
        print (ans[i],end=' ')

if __name__ == '__main__':
    smallest_prime_factor(10)