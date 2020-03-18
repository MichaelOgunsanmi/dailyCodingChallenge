# Source: https://leetcode.com/problems/binary-search-tree-iterator/
#
# Date: 14th August 2019


"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree. You may
assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when
next() is called. """


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.rootNode = root
        self.inOrderTraversal = []
        self.doInOrderTraversal(self.rootNode)
        self.index = -1

    def doInOrderTraversal(self, currentNode):
        if currentNode is None:
            return

        if currentNode.left is not None:
            self.doInOrderTraversal(currentNode.left)

        self.inOrderTraversal.append(currentNode.val)

        if currentNode.right is not None:
            self.doInOrderTraversal(currentNode.right)

    def next(self) -> int:
        self.index += 1
        return self.inOrderTraversal[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.inOrderTraversal)

    # Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
