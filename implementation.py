# implementation algorithm
### 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제


# 상하좌우
# N x N 크기의 정사각형 공간 위에 서 있습니다. 가장 왼쪽 위 (1, 1) 가장 오른쪽 아래(N, N)
r = (0, 1)
l = (0, -1)
u = (-1, 0)
d = (1, 0)

direction_table = {
    'R' : r,
    'L' : l,
    'U' : u,
    'D' : d
}

N = int(input())
moves = list(map(str, input().split()))
x, y = 1, 1

def canMove(x, y, N, d):
    newX = x + direction_table[d][0]
    newY = y + direction_table[d][1]

    if newX > N or newX < 1:
        return (False, x, y)
    elif newY > N or newY < 1:
        return (False, x, y)

    return (True, newX, newY)

for move in moves:
    result = canMove(x, y, N, move)
    print(result)
    if result[0]:
        x = result[1]
        y = result[2]

print(x, y)