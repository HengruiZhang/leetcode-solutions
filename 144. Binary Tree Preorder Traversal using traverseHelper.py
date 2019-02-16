# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res_list = []
        self.traverseHelper(root, res_list)
        return res_list

    def traverseHelper(self, root, res_l):
        if root == None:
            return
        res_l.append(root.val)
        self.traverseHelper(root.left, res_l)
        self.traverseHelper(root.right, res_l)