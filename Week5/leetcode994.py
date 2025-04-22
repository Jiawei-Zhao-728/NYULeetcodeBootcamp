from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        minutes = 0
        rotted = 0

        while queue:
            r, c, minute = queue.popleft()
            minutes = max(minutes, minute)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    rotted += 1
                    queue.append((nr, nc, minute + 1))

        return minutes if rotted == fresh else -1
