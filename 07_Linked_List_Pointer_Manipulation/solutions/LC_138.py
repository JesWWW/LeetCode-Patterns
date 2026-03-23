from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        curr = dummy
        old = head
        copy = {}
        while old:
            curr.next = Node(old.val)
            copy[old] = curr.next
            curr = curr.next
            old = old.next
        
        old = head
        curr = dummy
        while old:
            copy[old].random = copy.get(old.random)
            old = old.next
        return dummy.next