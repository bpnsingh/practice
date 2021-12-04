'''
Given a string A with start and end index s,e , reverser part of the substring.

'BIPINSINGH' 5   8
BIPINGINSH
'''
def swap(A,B):
    temp = B
    B = A
    A = temp
    return A,B
def solve(A,s,e):
    ans=list(A)
    while s < e :
        print (ans[s],ans[e])
        ans[s],ans[e]=swap(ans[s],ans[e])
        print (ans[s],ans[e])
        s+=1
        e-=1
    return "".join(ans)





if __name__ == '__main__':
    print (solve('BIPINSINGH',5,8))