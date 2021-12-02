'''
Given a string which contains lower case alphabets , sort these strings in dictionary order

input = 'dabaedb'
ouptout = 'aabbdde'
'''

def solve(A):
    N = len(A)
    ans=''
    f_array=[]
    for i in range(26):
        f_array.append(0)
    ascii_a = ord('a')
    #updating frequency of each character in array
    for char in A:
        index = ord(char) - ascii_a
        f_array[index] +=1
    for i in range(26):
        if f_array[i] > 0:
            for j in range(f_array[i]):
                ans=ans+chr(ascii_a+i)
    return ans





if __name__ == '__main__':
    print (solve('dabaedb'))