# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:


    def buildList(self, input: List[int] ):

        head = None

        for val in reversed(input):
            head = ListNode(val, head)

        return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # create head nodes for odd and even lists
        odd_head = None
        even_head = None
        curr_odd = None
        curr_even = None

        curr = head

        idx = 1

        # iterate through the list
        while curr is not None:
            # odd nodes
            if idx % 2 == 1:
                if curr_odd is None:
                    odd_head = ListNode(curr.val)
                    curr_odd = odd_head
                else:
                    curr_odd.next = ListNode(curr.val)
                    curr_odd = curr_odd.next
            # even nodes
            else:
                if curr_even is None:
                    even_head = ListNode(curr.val)
                    curr_even = even_head
                else:
                    curr_even.next = ListNode(curr.val)
                    curr_even = curr_even.next

            # advance node
            curr = curr.next
            idx += 1


        # rejoin lists
        if odd_head is not None:
            curr_odd.next = even_head
            return odd_head
        else:
            return even_head


if __name__ == '__main__':
    input = [1,2,3,4,5]

    sol = Solution()

    input = sol.buildList(input)

    output = sol.oddEvenList(input)

    print([e for e in output])
