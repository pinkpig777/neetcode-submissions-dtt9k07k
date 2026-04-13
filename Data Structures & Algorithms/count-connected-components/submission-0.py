class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        comp = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                comp += 1
        return comp
            
