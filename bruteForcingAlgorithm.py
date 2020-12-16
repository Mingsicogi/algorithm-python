# 완전 탐색 알고리즘
### 시각 - 00시 00분 00초 부터 N시 59분 59초까지 3포함된 모든 경우의 수는? (전체 데이터의 경우의 수가 86400개임)
print("---------------------- 시각 ----------------------")
N = int(input())
result = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                result += 1

print(result)


print("---------------------- 왕실의 나이트 ----------------------")
night_moves = [(2,1), (-2, 1), (2, -1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

position = input()
x = ord(position[0]) - ord('a') + 1
y = int(position[1])
result = 0

for night_move in night_moves:
    new_x = x + night_move[0]
    new_y = y + night_move[1]
    if new_x < 1 or new_x > 8 or new_y < 1 or new_y > 8:
        continue
    else:
        result += 1

print(result)


print("---------------------- 문자열 재정렬 ----------------------")
data = input()
result = []
value = 0

for char in data:
    if char.isalpha():
        result.append(char)
    else:
        value += int(char)

result.sort()

if value != 0:
    result += str(value)

print(''.join(result))