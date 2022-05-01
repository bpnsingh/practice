class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def middle_node(self, A):
        #check if node is empty
        if A is None:
            return
        #caculate len of LL
        slow = A
        fast = A
        cnt = 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, A):
        #If input LL is empty
        if A is None:
            return
        if A.next is None:
            return A
        #Lets B is head of reversed LL
        B = None
        #storing head to temp
        temp = A
        while temp:
            detached_node = temp
            temp = temp.next
            detached_node.next = B
            B = detached_node
        return B

    def reorderList(self, A):
        half1 = A
        A.print()
        slow = A
        fast = A
        cnt = 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        middle.print()
        '''
        print (middle)
        half2 = middle.next
        half2 = self.reverseList(half2)
        print (half2)
        temp1 = half1
        temp2 = half2
        while temp1 and temp2:
            temp1.next=temp2
            temp1= temp1.next
            temp2.next= temp1
            temp2=temp2.next

        return half1
        '''


if __name__ == '__main__':
    A = LinkedList()
    A.insert_values([1,2,3,4,5])
    A.print()
    scaler = Solution()
    scaler.reorderList(A)
