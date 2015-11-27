__author__ = 'FRAMGIA\nguyen.huy.quyet'

"""
session I
"""


class Node:
    """
    Class Node
    """

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node, data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        # if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node

    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        # if root is None or root is the search data.
        if node is None or node.data == data:
            return node

        if node.data < data:
            return self.search(node.right, data)
        else:
            return self.search(node.left, data)

    def deleteNode(self, node, data):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """

        # Check if tree is empty.
        if node is None:
            return None

        # searching key into BST.
        if data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else:  # reach to the node that need to delete from BST.
            if node.left is None and node.right is None:
                del node
            if node.left == None:
                temp = node.right
                del node
                return temp
            elif node.right == None:
                temp = node.left
                del node
                return temp

        return node

    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traverseInorder(root.left)
            print(root.data)
            self.traverseInorder(root.right)

    def traversePreorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            print(root.data)
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)

    def traversePostorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        if root is not None:
            self.traversePreorder(root.left)
            self.traversePreorder(root.right)
            print(root.data)


def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    print(root)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print("Traverse Inorder")
    tree.traverseInorder(root)

    print("Traverse Preorder")
    tree.traversePreorder(root)

    print("Traverse Postorder")
    tree.traversePostorder(root)


if __name__ == "__main__":
    main()

"""
session II
"""
# class Node:
#     def __init__(self, val):
#         self.l = None
#         self.r = None
#         self.v = val
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def getRoot(self):
#         return self.root
#
#     def add(self, val):
#         if (self.root == None):
#             self.root = Node(val)
#         else:
#             self._add(val, self.root)
#
#     def _add(self, val, node):
#         if (val < node.v):
#             if (node.l != None):
#                 self._add(val, node.l)
#             else:
#                 node.l = Node(val)
#         else:
#             if (node.r != None):
#                 self._add(val, node.r)
#             else:
#                 node.r = Node(val)
#
#     def find(self, val):
#         if (self.root != None):
#             return self._find(val, self.root)
#         else:
#             return None
#
#     def _find(self, val, node):
#         if (val == node.v):
#             return node
#         elif (val < node.v and node.l != None):
#             self._find(val, node.l)
#         elif (val > node.v and node.r != None):
#             self._find(val, node.r)
#
#     def deleteTree(self):
#         # garbage collector will do this for us.
#         self.root = None
#
#     def printTree(self):
#         if (self.root != None):
#             self._printTree(self.root)
#
#     def _printTree(self, node):
#         if (node != None):
#             self._printTree(node.l)
#             print(str(node.v) + ' ')
#             self._printTree(node.r)
#
#
# # 3
# # 0     4
# #   2      8
# # def main():
# tree = Tree()
# tree.add(3)
# tree.add(4)
# tree.add(0)
# tree.add(8)
# tree.add(2)
# tree.printTree()
# print(tree.find(3).v)
# print(tree.find(10))
# tree.deleteTree()
# tree.printTree()


# if __name__ == '__main__':
#     main()
