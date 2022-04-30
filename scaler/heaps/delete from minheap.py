'''
Implement insert value in min heap
'''
import heapq



class minheap:
    def swap(self,A,B):
        temp = A
        A = B
        B = temp
        return A,B
    def delete_min(self,A):
        '''
        This function delete minimum value of heap
        '''
        N = len(A)
        A[0],A[N-1] = self.swap(A[0],A[N-1])
        N = N - 1
        A = A[:N]
        print (A)
        i = 0
        while i<N:
            min = i
            l = (2*i) + 1
            r = (2*i) + 2
            print(i,l,r)
            if r<N and A[min] > A[r]:
                min = r
            if l<N and A[min] > A[l]:
                min = l
            if i == min:
                break
            A[i],A[min] = self.swap(A[i],A[min])
            print(A)
            i = min
        print(A)




scaler = minheap()
A= [2, 4, 3, 8, 7, 6, 9, 12, 10]
#heapq.heapify(A)
#print (A)

scaler.delete_min(A)
