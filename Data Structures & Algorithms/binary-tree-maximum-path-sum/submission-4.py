# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float("-inf")
        def dfs(node) -> int:
            if node == None:
                return 0
            
            left = max(dfs(node.left), 0)
            # print(left)
            right = max(dfs(node.right), 0)
            # print(right)
            local_sum = node.val + left + right
            self.max_path_sum = max(local_sum, self.max_path_sum)
            return node.val + max(right, left)
        dfs(root)
        return self.max_path_sum