'''
Given a string A of size N.
S= 'aBcDe'
o/p: 'AbCdE'
'''

def solve(A):
    ans=''
    for char in A:
        ans+=chr(ord(char)^32)
    return ans




if __name__ == '__main__':
    print (solve('aBcDe'))