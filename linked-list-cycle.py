# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == None:
                return True
            head.val = None
            head  = head.next
        return False

# without destroying traversed linked nodes
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if hasattr(head,'checked'):
                return True
            head.checked = 'checked'
            head = head.next

        return False