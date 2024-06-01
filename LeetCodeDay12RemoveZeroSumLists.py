# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def removeZeroSumSublists(self, head):
    dummy = ListNode(0)
    dummy.next = head
    seen = {}
    prefix = 0
    cur = dummy
    while cur:
        prefix += cur.val
        seen[prefix] = cur
        cur = cur.next
    prefix = 0
    cur = dummy
    while cur:
        prefix += cur.val
        cur.next = seen[prefix].next
        cur = cur.next
    return dummy.next

print(removeZeroSumSublists("self",[1,2,3,-3,4]))