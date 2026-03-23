# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy

        #Move before to the Node before left
        for _ in range(left-1):
            before = before.next
        first = before.next

        #Start to deal with reversing
        prev = None
        curr = first
        rev = right - left + 1 
        while rev and curr: 
            nxt = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nxt 
            rev -= 1
    
        first.next = curr
        before.next = prev

        return head