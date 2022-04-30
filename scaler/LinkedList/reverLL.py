# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        if A is None or B<2:
            return A
        if A.next is None:
            return A
        temp = A
        new_head = None
        last_node = None
        while temp and B > 0:
            swap_node = temp
            temp = temp.next
            swap_node.next  = new_head
            new_head = swap_node
            last_node = temp
            B -= 1
        return new_head,last_node
    def reverseBetween(self, A, B, C):
        if A is None or A.next is None or B == C:
            return A
        #BLN-->LN-->RN-->ARN
        BLN = None
        LN = A
        for i in range(B-1):
            BLN,LN = LN,LN.next
            LN = LN.next
        #logic for reversing
        temp = LN
        new_head = None
        ARN = None
        K = C -B +1
        while temp and K > 0:
            swap_node = temp
            temp = temp.next
            swap_node.next = new_head
            new_head = swap_node
            ARN = temp
            K -= 1
        RN = new_head
        if BLN:
            BLN.next=RN
        else:
            A = RN
        LN.next=ARN
        return A
