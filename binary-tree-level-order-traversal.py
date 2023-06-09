# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        layer = [root]
        while layer:
            layer_values = []
            next_layer = []
            for node in layer:
                layer_values.append(node.val)
                # check if there is a next layer
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            # add current layer to result list
            result.append(layer_values)
            # update layer to next layer to continue loop
            layer = next_layer
        return result
