from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev: Optional[ListNode] = None
        while head:
            succ: Optional[ListNode] = head.next
            head.next = prev
            prev = head
            head = succ
        return prev
