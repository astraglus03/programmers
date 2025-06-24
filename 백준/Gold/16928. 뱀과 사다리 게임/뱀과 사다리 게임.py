import sys
from collections import deque


def bfs(start,moves):
    queue = deque([(start,moves)])
    visited = [False] * 101
    visited[start] = True
    while queue:
        current, move = queue.popleft()

        if current ==100:
            print(move)
            return

        for i in range(1,7):
            next_pos = current + i

            if next_pos > 100:
                continue

            for ladder_start, ladder_end in ladders:
                if next_pos == ladder_start:
                    next_pos = ladder_end
                    break

            for snake_start, snake_end in snakes:
                if next_pos == snake_start:
                    next_pos = snake_end
                    break
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, move + 1))

ladder, snake = map(int, sys.stdin.readline().split())
ladders = deque()
snakes = deque()

for _ in range(ladder):
    start, end = map(int, sys.stdin.readline().split())
    ladders.append((start, end))

for _ in range(snake):
    start, end = map(int, sys.stdin.readline().split())
    snakes.append((start, end))

bfs(1,0)