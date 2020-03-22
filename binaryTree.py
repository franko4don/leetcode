import logging
from collections import deque
from copy import copy
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    """function to insert element in binary tree """

    def insertB(self, root, value):
        if root is None:
            return Node(value)
        q = []
        q.append(root)

        # Do level order traversal until we find
        # an empty place.
        while (len(q)):
            temp = q[0]
            q.pop(0)

            if temp.left is not None:
                temp.left = Node(value)
                break
            else:
                q.append(temp.left)

            if temp.right is not None:
                temp.right = Node(value)
                break
            else:
                q.append(temp.right)
        return temp

    def insert(self, node, value):
        if node is None:
            return Node(value)
        else:
            if value <= node.value:
                node.left = self.insert(node.left, value)
            else:
                node.right = self.insert(node.right, value)
        return node

    def insert_iterative(self, root, value):
        node = Node(value)

        if root is None:
            return node

        parent = None
        current = root

        while current is not None:
            parent = current
            if current.value < value:
                current = current.right

            else:
                current = current.left

        if parent.value <= value:
            parent.right = node

        else:
            parent.left = node

        return root

    def size(self, root):
        if root is None:
            return 0
        leftSize = self.size(root.left)
        rightSize = self.size(root.right)
        return leftSize + rightSize + 1

    def preorder_traversal(self, root):
        aroot = copy(root)
        stack = deque()
        if root is None:
            return
        stack.append(root)
        while len(stack) != 0:
            root = stack.pop()
            print(root.value)
            if root.right is not None:
                stack.append(root.right)

            if root.left is not None:
                stack.append(root.left)

    def inorder_traversal(self, root):
        stack = deque()
        if root is None:
            return

        while True:
            if root is not None:
                stack.append(root)
                root = root.left

            else:
                if len(stack) == 0:
                    break
                root = stack.pop()
                print(root.value)
                root = root.right

    def postorder_traversal(self, root):
        stack = deque()
        result = []
        if root is None:
            return
        stack.append(root)
        while len(stack) != 0:
            root = stack.pop()
            result.insert(0, root.value)
            if root.left is not None:
                stack.append(root.left)

            if root.right is not None:
                stack.append(root.right)
        return result

    def levelorder_traversal(self, root):
        stack = deque()
        result = []
        general = []

        if root is None:
            return
        stack.append(root)
        while len(stack) != 0:
            root = stack.popleft()

            result.append(root.value)

            if root.left is not None:
                stack.append(root.left)


            if root.right is not None:
                stack.append(root.right)

    def lca(self, root, p, q):
        if root is None:
            return None
        if root is p or root == q:
            return root
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if left is not None and right is not None:
            return root
        if left is None and right is None:
            return None

        return left if left is not None else right


    def traversal(self, root):
        stack = deque()
        result = []
        if root is None:
            return
        stack.append(root)
        while len(stack) != 0:
            root = stack.popleft()
            result.append(root.value if root is not None else None)
            if root is not None:
                if root.left is not None:
                    stack.append(root.left)
                    if root.right is None:
                        stack.append(None)

                if root.right is not None:
                    stack.append(root.right)
                    if root.left is None:
                        stack.append(None)

        if len(result) == 0:
            return True
        i = 1
        j = 1
        general = []
        result.insert(0, -34)
        while i < len(result):
            j *= 2
            print(i, j, result[i:j])
            if i < len(result):
                k = result[i:j]
                k.reverse()
                general.extend(k)
            i *=2

        k = result[i: len(result)]
        k.reverse()
        general.extend(k)
        result.pop(0)
        return general == result


    def height(self, node):

        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            # Use the larger one
            return max(lheight, rheight) + 1


    def inOrderTraversal(self, node):

        if node:
            if node.left is None and node.right is not None:
                print(0)
            if node.right is None and node.left is not None:
                print(0)
            print(node.value)
            self.inOrderTraversal(node.left)

            self.inOrderTraversal(node.right)

m = None
tree = BinaryTree()
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
print(tree.traversal(m))
print(tree.height(m))
# [5,4,8,11,null,13,4,7,2,null,null,null,1]
# m = tree.insert(m, 5)
# m = tree.insert(m, 4)
# m = tree.insert(m, 8)
# m = tree.insert(m, 11)
# m = tree.insert(m, None)
# m = tree.insert(m, 13)
# m = tree.insert(m, 4)
# m = tree.insert(m, 7)
# m = tree.insert(m, 2)
# m = tree.insert(m, None)
# m = tree.insert(m, None)
# m = tree.insert(m, None)
# m = tree.insert(m, 1)

# tree.preorder_traversal(m)
# tree.inorder_traversal(m)
# print(tree.inorder_traversal(m))
# print(tree.levelorder_traversal(m))

# print(serialize(root))
