# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # mid, left, right
        # left, mid, right
        #[1, 2, 3, 4]
        #[2, 1, 3, 4]
        inorder_map = {}
        for id, val in enumerate(inorder):
            inorder_map[val] = id
        self.pre_id = 0
        def dfs(l, r):
            if l > r:
                return None
            
            root_val = preorder[self.pre_id]
            self.pre_id += 1
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        return dfs(0, len(inorder)-1)
            