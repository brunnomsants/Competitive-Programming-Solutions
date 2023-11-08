from collections import deque

movsbunnies = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

def movs(row, col, m):
    rows = len(m)
    columns = len(m[0])
    arr = []
    for _ in range(rows):
        arr.append([None] * columns)
    arr[row][col] = 1
    queue = deque()
    queue.append((row, col))

    while queue:
        r, c = queue.popleft()
        for dr, dc in movsbunnies:
            nr, nc = (r + dr, c + dc)
            if 0 <= nr < rows and 0 <= nc < columns and arr[nr][nc] is None:
                arr[nr][nc] = arr[r][c] + 1
                if m[nr][nc] != 1:
                    queue.append((nr, nc))
    return arr


def solution(m):
    rows = len(m)
    columns = len(m[0])
    source = movs(0, 0, m)
    dest = movs(rows - 1, columns - 1, m)
    result = 20 * 20 + 1
    for i in range(rows):
        for j in range(columns):
            if source[i][j] and dest[i][j]:
                result = min(result, source[i][j] + dest[i][j] - 1)
                if result == rows + columns - 1:
                    return result
    return result
