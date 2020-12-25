from collections import deque

# basic algorithm for DFS_BFS

### stack
print("------------------ STACK -----------------")
stack = []

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')

print("stack before pop :", stack)
print("pop from stack :", stack.pop())
print("stack after pop :", stack)
print("stack print from top :", stack[::-1])


### queue
print("------------------ QUEUE -----------------")
from collections import deque

queue = deque()
queue.append('A')
queue.append('B')
queue.append('C')
queue.append('D')


print("queue before pop :", queue)
print("pop from queue :", queue.popleft())
print("queue after pop :", queue)
queue.reverse()
print("queue print from top :", queue)


print("------------------ Recursive Function -----------------")
def recursive_function(r):
    if r == 5:
        return
    else:
        print("Call recursive function")
        recursive_function(r + 1)

recursive_function(0)

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)

print(factorial(5))

# 유클리드 호제법. A, B의 최대 공약수(A>B) A를 B로 나눈 나머지를 R이라고 하면 A와 B의 최대 공약수는 B와 R의 최대 공약수와 같다.
print("----- Euclidean algorithm -----")
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(162, 192))


# DFS - Stack 활용 - 마지막 노드 depth까지 탐색하여 처리함.
print("------------------ DFS -----------------")
def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' -> ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * len(graph)

dfs(graph, 1, visited)


# BFS - Queue 활용 - 인접한 노드를 한번에 큐에 저장함.
print("\n------------------ BFS -----------------")
visited = [False] * len(graph)
def bfs(graph, v, visited):
    queue = deque()

    queue.append(v)
    visited[v] = True

    while queue:
        node = queue.popleft()
        print(node, end=" -> ")

        for sub_node in graph[node]:
            if not visited[sub_node]:
                visited[sub_node] = True
                queue.append(sub_node)

bfs(graph, 1, visited)
print('\n')


# 음료수 얼려 먹기 - connected component
n, m = map(int, input().split()) # N x M 입력을 받기 위함.
graph = [] 
for i in range(n): # n 행 만큼
    graph.append(list(map(int, input()))) # 공백없이 받은 값을 정수형 배열로 append
print(graph)

def dfs_2(x, y):
    if x < 0 or x >= n or y < 0 or y >= m: # N x M 을 벗어나면 false 
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1 # 0인 지점은 방문 처리를 하고,

        # 방문한 지점 상하좌우로 방문
        dfs_2(x - 1, y) 
        dfs_2(x + 1, y)
        dfs_2(x, y - 1)
        dfs_2(x, y + 1)

        return True # 주변에 추가적으로 0인 지점이 있어도, 하나로 처리됨.

    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs_2(i, j):
            result += 1

print(result)


# 미로 탈출 -> BFS 간선의 비용이 모두 같을때 최소 비용을 구하기 위해 사용할 수 있음
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_3(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        print(queue)
        x, y = queue.popleft()
        for i in range(4):
            xn = x + dx[i]
            yn = y + dy[i]

            if xn < 0 or xn >= m or yn < 0 or yn >= n:
                continue

            if graph[xn][yn] == 0:
                continue

            if graph[xn][yn] == 1:
                graph[xn][yn] = graph[x][y] + 1
                queue.append((xn, yn))

    return graph[n - 1][m - 1]


print(dfs_3(0,0))
