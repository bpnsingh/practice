'''
Problem Description

Given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
'''
def swap(A,B):
    temp = B
    B = A
    A = temp
    return A,B

def reverse_substring(A,s,e):
    ans=list(A)
    while s < e :
        ans[s],ans[e]=swap(ans[s],ans[e])
        s+=1
        e-=1
    return "".join(ans)

def reverse_string(A):
    ans = ''
    N = len(A)
    for i in range(N - 1, -1, -1):
        ans += A[i]
    return ans

def solve(A):
    r_string = reverse_string(A)
    ans = list(r_string)
    #print(ans)
    N = len(r_string)
    print(N)
    s = 0
    for i in range(N):
        if ans[i] == " " or i == N-1:
            print(s,i-1)
            if i < N -1:
                e = i -1
            else:
                e = i
            ans=reverse_substring(ans,s,e)
            s=i+1
    return "".join(ans)




if __name__ == '__main__':
    print (solve('sky is blue'))