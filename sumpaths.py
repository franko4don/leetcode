# Definition for a binary tree node.
from collections import deque
from copy import copy


class TreeNode:
    def __init__(self, x):
        self.value = x
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

    def preorder_traversal(self, root):
        aroot = copy(root)
        stack = deque()
        path = []
        if root is None:
            return
        stack.append(root)
        while len(stack) != 0:
            root = stack.pop()

            print(root.value)
            path.append(root.value)
            if root.right is not None:
                stack.append(root.right)
                print(path)
                path.clear()
            if root.left is not None:
                stack.append(root.left)
                print(path)
                path.clear()


    def inOrderTraversal(self, node, a, sum):

        if node:
            a += node.value
            if node.left is None and node.right is None:
                if a == sum:

                    return True
                return
            self.inOrderTraversal(node.left, a, sum)
            self.inOrderTraversal(node.right, a, sum)
        # print(path)

    def buildTree(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.left.right = TreeNode(1)
        return root


m = None
tree = Solution()
r = tree.buildTree()
# tree.preorder_traversal(r)
print(tree.inOrderTraversal(r, 0, 22))
