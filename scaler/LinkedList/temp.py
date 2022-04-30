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
    def print_ll(node1):
        # Output each element followed by a space
        if node1 is None:
            return
        itr = node1
        while itr:
            if itr.next is None :
                print (itr.data)
            else:
                print (itr.data,end=' ')
            itr = itr.next
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
        RN, ARN = self.reverseList(LN,C-B+1)
        self.print_ll(RN)
        if BLN:
            BLN.next=RN
        else:
            A = RN
        LN.next=ARN
        return A
