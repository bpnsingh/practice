from LL import LinkedList
def reverseLL(A):
    temp = A.head
    if temp is None or temp.next is None:
        return A
    B = None
    while temp:
        new_node = temp
        temp = temp.next
        new_node.next = B
        B = new_node
    return

ll = LinkedList()

ll.insert_values([45,7,12,567,99])
#ll.print()
middle= (ll.get_middle)
middle.print()