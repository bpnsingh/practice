'''
Given an array of integers A, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.
Find and return the number of permutations of A that are squareful. Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].
Problem Constraints
1 <= length of the array <= 12
1 <= A[i] <= 109
Input Format
The only argument given is the integer array A.
Output Format
Return the number of permutations of A that are squareful.
Example Input
Input 1:
 A = [2, 2, 2]
Input 2:
 A = [1, 17, 8]
Example Output
Output 1:
 1
Output 2:
 2
Example Explanation
Explanation 1:
 Only permutation is [2, 2, 2], the sum of adjacent element is 4 and 4 and both are perfect square.
Explanation 2:
 Permutation are [1, 8, 17] and [17, 8, 1].
'''
import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def check_square(self,num):
        mul = int(math.sqrt(num))
        print (mul,num)
        return mul*mul == num
    def solve(self, A):
        global cnt
        cnt = 0

        temp_list = []
        freq = {n:0 for n in range(max(A)+1)}
        for num in A:
            freq[num] += 1
        #print (freq)
        def check():
            global cnt
            if len(temp_list) == len(A):
                print(temp_list)
                sum = 0
                flag = False
                for i in range(1,len(temp_list)):
                    if self.check_square(temp_list[i-1]+temp_list[i]):
                        print ("inside")
                        flag = True
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    cnt+=1
                    print("cnt is updated")
                return

            for num in freq:
                if freq[num] > 0:
                    temp_list.append(num)
                    freq[num] -= 1
                    check()
                    temp_list.pop()
                    freq[num] += 1
        check()
        return cnt
scaler = Solution()
A= [1,17,8]
#A= [41]
print(scaler.solve(A))