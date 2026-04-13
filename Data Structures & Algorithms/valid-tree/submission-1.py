class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Check connected
        if len(edges) != n-1:
            return False
        # Check acyclic
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return True
                if dfs(nei, node):
                    return True # cycle detected
            return False
        
        for i in range(n):
            if i not in visited:
                if dfs(i, -1):
                    return False
        return True