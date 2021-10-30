# Definition for singly-linked list.
from LinkedLists.ReverseLinkedList import ListNode

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    head = None
    if l1 is None and l2 is None:
        return None
    if l1 is None:
        head = ListNode(l2.val)
        l2 = l2.next
    elif l2 is None:
        head = ListNode(l1.val)
        l1 = l1.next
    elif (l1.val < l2.val):
        head = ListNode(l1.val)
        l1 = l1.next
    else:
        head = ListNode(l2.val)
        l2 = l2.next

    curr = head

    while l1 is not None or l2 is not None:
        if l1 is None:
            curr.next = ListNode(l2.val)
            l2 = l2.next
        elif l2 is None:
            curr.next = ListNode(l1.val)
            l1 = l1.next

        elif(l1.val < l2.val):
            curr.next = ListNode(l1.val)
            l1 = l1.next
        else:
            curr.next = ListNode(l2.val)
            l2 = l2.next

        curr = curr.next

    return head
