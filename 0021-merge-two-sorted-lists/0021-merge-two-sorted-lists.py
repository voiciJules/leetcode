# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current_node = head

        while list1 and list2:
            if list1.val <= list2.val:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
                
            current_node = current_node.next
            
        if list1:
            current_node.next = list1
        else:
            current_node.next = list2
        
        return head.next

        # I wrote the first line like the below
        # current_node = ListNode()

        # But, I should have to write the first part like the below. 
        # head = ListNode()
        # current_node = head

        # after finishing the codes, I have to return it. When I returned 'current_node', it returned only [4, 4]. because the current position of current_node is 4 and the next is 4. I saw the solution of others and I realized we have to have head for the first position to return.
        # When you return head
        # the answer is [0,1,1,2,3,4,4]. It includes [0]. 
        # to return without the head value, we have to return head.next 
