class Node:
    def __init__(self, val=None,next=None):
        self.val = val
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
            llstr += str(itr.val)+' --> ' if itr.next else str(itr.val)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, val):
        node = Node(val, self.head)
        self.head = node
    def get_middle(self):
        if self.head is None:
            return
        temp = self.head
        slow= temp
        fast=temp
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        return slow.head

    def insert_at_end(self, val):
        if self.head is None:
            self.head = Node(val, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(val, None)

    def insert_at(self, index, val):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(val)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(val, itr.next)
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

    def insert_values(self, val_list):
        self.head = None
        for val in val_list:
            self.insert_at_end(val)





if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()

