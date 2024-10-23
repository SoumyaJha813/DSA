# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        llist3 = ListNode()
        head3 = llist3
        hh = llist3
        print(head1)
        print(head2)
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                head3.next =  head1
                head1 = head1.next
            elif head2.val <= head1.val:
                head3.next = head2
                head2 = head2.next
            head3 = head3.next
        if head1 is not None:
            head3.next = head1
        elif head2 is not None:
            head3.next = head2
        return hh.next

        
