# Source: https://leetcode.com/problems/construct-string-from-binary-tree/
#
# Level: Easy
#
# Date: 30th July 2019


"""
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""


# Solution


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""

        return "".join(treeToString(t, []))[1:-1]


def isLeaf(currentNode):
    return currentNode.left is None and currentNode.right is None


def treeToString(currentNode, output):
    if isLeaf(currentNode):
        output.append('({value})'.format(value=currentNode.val))
        return output

    output.append('({value}'.format(value=currentNode.val))

    if currentNode.left is None:
        output.append('()')
    else:
        treeToString(currentNode.left, output)

    if currentNode.right is not None:
        treeToString(currentNode.right, output)

    output.append(')')

    return output
