'''
Given an array N and Q queries , find the frequency of all given queries
'''

def frequency_dict(A,B):
    ans={}
    for num in A:
        if num in ans:
            ans[num]+=1
        else:
            ans[num] = 1
    for q in B:
        print (ans[q])

if __name__ == '__main__':
    A= [2,6,3,8,2,8,2,3,8]
    B=[8,3,2]
    print(frequency_dict(A,B))
