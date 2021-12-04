'''
given an array of size N, find the first non repeating element
IP:[8,2,8,3,1,2,6,5]
op=3
'''

'''
Approach:
first count the frequency of each number(buid a frequency array)
then iterate though array and check which number has frquency =1 and return It
'''

def freq_dict(A):
    ans={}
    for item in A:
        if item not in ans:
            ans[item] = 1
        else:
            ans[item] += 1
    return ans

def solve(A):
    frq_array=freq_dict(A)
    for num in A:
        if frq_array[num] == 1:
            return num
    return 0
if __name__ == '__main__':
    A=[8,2,8,3,1,2,6,5]
    print(solve(A))