# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # edge casess
        if not head or not head.next or k == 0:
            return head

        #Count the length of the list
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head # make it circular

        # If it turn out to rotate one cycle
        k %= n
        if k == 0:
            return head
        
        # Find the new tail and head
        tail = head
        for _ in range(n-k-1):
            tail = tail.next
        head = tail.next
        tail.next = None

        return head