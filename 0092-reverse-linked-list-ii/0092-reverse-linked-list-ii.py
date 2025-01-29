# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        reverse = []
        
        current = head
        current2 = head
        
        j=1
        while j < right + 1: 
            if j >= left and j <= right:
                reverse.append(current.val)
            current = current.next
            j += 1
        
        i=1
        while i < right + 1:
            if i >= left and i <= right:
                current2.val = reverse.pop()
            current2 = current2.next
            i += 1
        
        return head