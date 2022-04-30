class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
node1 = None
global node1

def get_length():
        global node1
        count =0
        itr = node1
        while itr:
            count+=1
            itr=itr.next
        return count

def insert_node(position, value):
    global node1
    position = position -1
    if position < 0 or position > get_length():
            return

    if position ==0:
        node=Node(value,node1)
        node1=node
        return

    count = 0
    itr = node1
    while itr:
        if count == position -1:
            node=Node(value,itr.next)
            itr.next=node
            break
        count+=1
        itr=itr.next


def delete_node(position):
    global node1
    position=position-1
    if position < 0 or position >= get_length():
        return
    if position == 0:
        node1=node1.next
        return

    itr=node1
    count =0
    while itr:
        if count == position-1:
            if itr.next != None:
                itr.next=itr.next.next
            break
        count+=1
        itr=itr.next


def print_ll():
    global node1
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
