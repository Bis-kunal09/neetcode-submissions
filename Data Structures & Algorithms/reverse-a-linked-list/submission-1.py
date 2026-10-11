# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    
    def f(self,head):
        if head==None or head.next==None:
            return head
        
        new_head=self.f(head.next)
        head.next.next=head
        head.next=None
        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
    
        
        return self.f(head)

        