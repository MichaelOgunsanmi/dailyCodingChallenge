# Source: https://leetcode.com/problems/leaf-similar-trees/

# Level: Easy
#
# Date: 08th August 2019


"""Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value
sequence.


For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Note:

Both of the given trees will have between 1 and 100 nodes.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        root1Leaves = []
        getLeaves(root1, root1Leaves)
        root2Leaves = []
        getLeaves(root2, root2Leaves)

        if len(root1Leaves) != len(root2Leaves):
            return False

        for i in range(len(root1Leaves)):
            if root1Leaves[i] != root2Leaves[i]:
                return False

        return True


def getLeaves(currentNode, leafNodes):
    if currentNode is None:
        return

    if isLeaf(currentNode):
        leafNodes.append(currentNode.val)
        return

    if currentNode.left is not None:
        getLeaves(currentNode.left, leafNodes)

    if currentNode.right is not None:
        getLeaves(currentNode.right, leafNodes)

    return


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None
