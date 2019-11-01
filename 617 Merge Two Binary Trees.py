# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):                      
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # new Tree node
        node = t1
        # return self.merge(t1,t2)
        if t1 == None and t2 == None:
            return None
        elif t1 == None and t2 != None:
            return t2
        elif t1 != None and t2 == None:
            return t1
        elif t1 != None and t2 != None:
            node.val = t1.val + t2.val
        node.left = self.mergeTrees(t1.left,t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        
        return node
        
