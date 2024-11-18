# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        h2 = l2
        num1 = 0
        num2 = 0
        count1 = 0
        count2 = 0
        
        while h1:
            rem1 = h1.val
            num1 = num1 + rem1*pow(10,count1)
            count1 += 1
            h1 = h1.next
        print("Num1: ", num1)
        while h2:
            rem2 = h2.val
            num2 = num2 + rem2*pow(10,count2)
            count2 += 1
            h2 = h2.next
        print("Num2: ", num2)
        total = num1 + num2
        total = str(total)
        total = total[::-1]
        def createlinkedlist(total):
            h3 = None
            current_node = None
            for s in total:
                newnode = ListNode(int(s))
                if h3 is None:
                    h3 = newnode
                    current_node = h3
                else:
                    current_node.next = newnode
                    current_node = newnode
            return h3
        llist = createlinkedlist(total)
        def displaylinkedlist(llist):
            h4 = llist
            while h4:
                print(h4.val)
                h4 = h4.next
        displaylinkedlist(llist)
        return llist
