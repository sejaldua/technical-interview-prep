# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        res = head
        while l1 and l2:
            print("LL1:", l1.val, l1.next)
            print("LL2:", l2.val, l2.next)
            print("--------")
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                res.next = l2
                l2 = l2.next
            res = res.next
            
        # exactly one of l1 and l2 can be non-null at this point, so
        # connect the non-null list to the end of the merged list
        res.next = l1 if l1 is not None else l2
        
        return head.next
        
        
