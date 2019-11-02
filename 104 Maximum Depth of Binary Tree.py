# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # we can traverse per level and keep the heigh in an updated variable so that when we exit we could return just the variable itself
           # base case
        if root is None:
            return 0 # depth == 0
        # this is the iterative apporach should consider doing the recurrsive 
        current = [root]
        depth = 0
        while current:
            depth += 1
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
        return depth
