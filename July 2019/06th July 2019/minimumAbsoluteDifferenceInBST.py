'''
Source: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Level: Easy

Date: 06th July 2019, 2019

'''

''' 
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note: There are at least two nodes in this BST.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, rootNode):
        minDifference = float('inf') 
        
        currentNode = rootNode
        stack = []
        treeElements = []
        
        while True:
            if currentNode != None:
                stack.append(currentNode)
                prevNode = currentNode
                currentNode = currentNode.left 
            else:
                if len(stack) == 0:
                    break 
                currentNode = stack.pop()
                treeElements.append(currentNode.val)
                currentNode = currentNode.right
                
        for i in range(len(treeElements)):
            if i + 1 < len(treeElements) and abs(treeElements[i] - treeElements[i+1]) < minDifference:
                minDifference = abs(treeElements[i] - treeElements[i+1])
        
        return minDifference
            
        
        