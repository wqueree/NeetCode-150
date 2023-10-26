from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.depth(root.left), self.depth(root.right)) if root else 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode], max_diameter: int = 0) -> int:
        if not root:
            return max_diameter
        diameter = self.depth(root.left) + self.depth(root.right)
        max_diameter = max(max_diameter, diameter)
        return max(self.diameterOfBinaryTree(root.left, max_diameter), self.diameterOfBinaryTree(root.right, max_diameter))
