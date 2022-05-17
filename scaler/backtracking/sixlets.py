class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def sum(self,A,index,temp_list,B):
        if index == len(A):
            if len(temp_list) == B:
                sum = 0
                for num in temp_list:
                    sum += num
                global cnt
                if sum <= 1000:
                    cnt+=1
            return
        temp_list.append(A[index])
        self.sum(A,index+1,temp_list,B)
        temp_list.pop()
        self.sum(A,index+1,temp_list,B)
    def solve(self, A, B):
        global cnt
        cnt = 0
        self.sum(A,0,[],B)
        return cnt

scaler = Solution()
A = [1,2,8]
print(scaler.solve(A,2))