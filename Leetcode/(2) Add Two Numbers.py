# https://leetcode.com/problems/add-two-numbers/

from ds import ListNode

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new = ListNode(None)
        base = new
        add = 0
        while not (l1 is None and l2 is None) or add != 0:
            if l1 is not None and l2 is not None:
                new.val = l1.val + l2.val + add
                l1 = l1.next
                l2 = l2.next
            elif l1 is None and l2 is not None: #l2 not none
                new.val = l2.val + add
                l2 = l2.next
            elif l2 is None and l1 is not None: #l1 not none
                new.val = l1.val + add
                l1 = l1.next
            else:#only add
                new.val = add

            add = 0
            if new.val >= 10:
                add = 1
                new.val -= 10
            
            if not (l1 is None and l2 is None) or add != 0:
                new.next = ListNode(None)
                new = new.next

        return base