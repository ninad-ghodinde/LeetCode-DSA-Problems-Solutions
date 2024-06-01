# Definition for a binary tree node.

####################################################not solved
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #return 0

        n1=TreeNode(1)
        n2=TreeNode(2)
        n3=TreeNode(3)
        n4=TreeNode(4)
        n5=TreeNode(5)

        n1.left=n2
        n1.right=n3
        n2.left=n4
        n2.right=n5
        print(n1)
        
        
print(Solution().diameterOfBinaryTree([1,2,3,4,5]))

    
        