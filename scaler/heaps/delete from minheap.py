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
        A[0],A[N-1] = A[N-1],A[0]
        N = N - 1
        A = A[:N]
        print (A)
        i = 0
        while i<N:
            min = i
            l = (2*i) + 1
            r = (2*i) + 2
            if r<N and (A[min] > A[r]) and (A[r] < A[l]):
                min = r
            if l<N and A[min] > A[l] and (A[l] < A[r]):
                min = l
            if i == min:
                break
            A[i],A[min] = A[min],A[i]
            print(A)
            i = min
        print(A)
        heapq.heapify(A)
        print(A)




scaler = minheap()
A= [2, 4, 3, 8, 7, 6, 9, 12, 10]
#heapq.heapify(A)
#print (A)

scaler.delete_min(A)
