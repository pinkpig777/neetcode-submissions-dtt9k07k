class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            if node == parent:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei, node)
            
        
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1
        return res