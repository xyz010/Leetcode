# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # base case
        if root is None:
            return []
        # this is the iterative apporach should consider doing the recurrsive 
        result,current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            length = float(len(vals))
            result.append(sum(vals)/length)
        return result

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input

def doubleListToString(nums, len_of_list=None):
    if nums is None or len_of_list == 0:
        return "[]"

    if len_of_list is None:
        len_of_list = len(nums)

    serializedDoubles = []
    for num in nums:
        serializedDoubles.append(doubleToString(num))
    return "[{}]".format(','.join(serializedDoubles))

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            root = stringToTreeNode(line)
            
            ret = Solution().averageOfLevels(root)

            out = doubleListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
