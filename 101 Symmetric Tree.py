# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def check(self,leftSub, rightSub):
        if leftSub == None and rightSub == None:
            return True
        elif leftSub != None and rightSub != None:
            return leftSub.val == rightSub.val and self.check(leftSub.left, rightSub.right) and self.check(leftSub.right, rightSub.left)
        return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # we will now perform the recursive function
        return root == None or self.check(root.left, root.right)
