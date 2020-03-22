# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insert(self, node, value):
        if node is None:
            return TreeNode(value)
        else:
            if value <= node.value:
                node.left = self.insert(node.left, value)
            else:
                node.right = self.insert(node.right, value)
        return node

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        aroot = root
        if root is None:
            return False
        stack = deque()
        stack.append(root)

        while len(stack) != 0:
            root = stack.pop()
            if root.left is not None:
                aroot.left = TreeNode(root.val + root.left.val)
                root = root.left

                stack.append(root)

m = None
tree = Solution()
m = tree.insert(m, 8)
m = tree.insert(m, 3)
m = tree.insert(m, 6)
m = tree.insert(m, 10)
m = tree.insert(m, 4)
m = tree.insert(m, 7)
m = tree.insert(m, 1)
m = tree.insert(m, 14)
m = tree.insert(m, 13)
m = tree.insert(m, 18)
m = tree.insert(m, 19)