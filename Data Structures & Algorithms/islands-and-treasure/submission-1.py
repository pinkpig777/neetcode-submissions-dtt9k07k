class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multisource BFS
        m = len(grid)
        n = len(grid[0])
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    # print(f"(r: {r} , c: {c})")
                    q.append((r,c))
        while q:
            q_len = len(q)
            # print(f"q_len: {q_len}")
            for i in range(q_len):
                row, col = q.popleft()
                for dr, dc in DIR:
                    nr = row + dr
                    nc = col + dc
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == INF:
                        q.append((nr, nc))
                        grid[nr][nc] = grid[row][col] + 1
        
