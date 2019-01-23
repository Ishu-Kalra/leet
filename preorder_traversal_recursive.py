class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.dfs(root,ans)
        return ans
    
    
    def dfs(self,root,ans):
        if not root:
            return 
        ans.append(root.val)  #中序遍历
        self.dfs(root.left,ans)
        self.dfs(root.right,ans)