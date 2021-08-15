from ReverseLinkedList import ListNode
def isPalindrome(head: ListNode) -> bool:

    vals = []

    while head is not None:
        vals.append(head.val)
        head = head.val
    l = len(vals) - 1
    for i in range(l/2):
        if vals[i] != vals[l - i]:
            return False

    return True
