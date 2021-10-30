# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def initLinkedList(vals):

    if len(vals) == 0:
        return(ListNode)

    vals.reverse()

    next = None
    for val in vals:
        curr = ListNode(val)
        curr.next = next
        next = curr

    return curr

def printLinkedList(head: ListNode) -> None:


    vect = []

    while head is not None:
        vect.append(head.val)
        head = head.next

    print(vect)






def reverseList(head: ListNode) -> ListNode:

    curr = head
    head = ListNode(curr.val)

    while curr.next is not None:
        head = ListNode(curr.next.val, head)
        curr = curr.next

    return head


