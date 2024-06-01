# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        print(head)
        n = 10  # Example: Loop from 10 down to 1
        for i in range(5, 1, -1):
            print(i)
        #print(head[0], head[-1])
        main=[]
        while len(head)>1:
            print(head[0], head[-1])
            main.append(head[0])
            main.append(head[-1])
            head=head[1:-1]
        if len(head)==1:
            return main.append(head[0])
        else:
            return main
            
print(Solution.isPalindrome(Solution, [1,2]))