class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        #Optimised appproach
        #initaalise frequency dictionaty
        freq_mod = dict()
        for num in range(B):
            freq_mod[num] = 0
        print(freq_mod)
        #update frequency of numbers of mod
        for num in A:
            freq_mod[num%B] += 1
        print(freq_mod)
        ans = (freq_mod[0]*freq_mod[0] -1)//2
        i = 1
        j = B -1
        while i <j:
            if i == j:
                ans += (freq_mod[i]*freq_mod[i] -1)//2
            ans += freq_mod[i]*freq_mod[j]
            i = i+1
            j = j -1
        return ans

scaler = Solution()
A = [1, 2, 3, 4, 5]
B = 2
#A = [2,7,5,10,8,4,6,11]
#B = 5
print(scaler.solve(A, B))