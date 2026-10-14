n, m = map(int, input().split())
k = int(input())
bomb_coordinate = []
for i in range(k):
    x, y = map(int, input().split())
    bomb_coordinate.append((x, y))

board = []
for x in range(n):
    board.append([])
    for y in range(m):
        board[x].append(0)

for coordinate in bomb_coordinate:
    x, y = coordinate
    board[x - 1][y - 1] = "*"


def chek_bomb(x, y):
    pos = [-1, 0, 1]

    if board[x - 1][y - 1] != "*":
        for i in pos:
            for j in pos:
                if i != 0 or j != 0:
                    nx = x - 1 + i
                    ny = y - 1 + j

                    if 0 <= nx < n and 0 <= ny < m:
                        if board[nx][ny] == "*":
                            board[x - 1][y - 1] += 1


for x in range(n):
    for y in range(m):
        chek_bomb(x + 1, y + 1)

for row in board:
    print(" ".join(map(str, row)))
