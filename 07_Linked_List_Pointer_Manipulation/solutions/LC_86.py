from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        tail1 = dummy1
        tail2 = dummy2
        curr = head

        while curr:
            nxt = curr.next
            if curr.val < x:
                tail1.next = curr
                tail1 = tail1.next
            else:
                tail2.next = curr
                tail2 = tail2.next
            curr = nxt
        tail2.next = None
        tail1.next = dummy2.next
        
        return dummy1.next