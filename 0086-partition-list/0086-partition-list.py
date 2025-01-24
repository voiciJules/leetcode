# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        current = head
        
        lessThan = ListNode()
        lessThan_head = lessThan

        greaterOrEqual = ListNode()
        greaterOrEqual_head = greaterOrEqual

        output = lessThan

        while current:
            if current.val < x:
                lessThan.next = ListNode(current.val)
                lessThan = lessThan.next
            else:
                greaterOrEqual.next = ListNode(current.val)
                greaterOrEqual = greaterOrEqual.next
            current = current.next
        
        lessThan.next = greaterOrEqual_head.next
        
        return output.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


