from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []

        def inOrder(root):
            # base case:
            if not root:
                return None

            # check if there is left node to handle
            inOrder(root.left)

            # push current node after left handled
            arr.push(root)

            # check if there is right node to handle
            inOrder(root.right)

        inOrder(root)
        # final array must be sorted with no duplicates
        return True if arr == list(sorted(set(root))) else False
