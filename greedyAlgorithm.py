# greedy algorithm
### 현재 상황에서 지금 당장 좋은 것만 고르는 방법을 의미함.
### 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구함
### 그리디 해법은 그 정당성 분석이 중요함. 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토.

print("---------------------- 거스름돈 문제 ----------------------")
coins = [500, 100, 50, 10]

def minChangeCoinCount(money):
    changeCoinCount = 0
    for coin in coins:
        changeCoinCount += money // coin
        money %= coin
    return changeCoinCount

print(minChangeCoinCount(1260))


print("---------------------- 1이 될 때까지 ----------------------")
n, k = map(int, input().split())
result = 0
while True:
    target = (n // k) * k # k로 나눠 떨어지는 n에 가까운 가장 큰 수 = target
    result += (n - target) # 1을 빼는 횟수를 한번에 계산
    n = target

    if n < k:
        break

    result += 1
    n //= k

result = result + n - 1
print(result)

print("---------------------- 곱하기 혹은 더하기 ----------------------")
data = input()
result = int(data[0])

for i in range(1, len(data)):
    num_data = int(data[i]) 
    if num_data <= 1 or result <= 1:
        result += num_data
    else:
        result *= num_data

print(result)


print("---------------------- 모험가 길드 ----------------------")

n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0
count = 0

for data in array:
    count += 1
    if count >= data:
        result += 1
        count = 0

print(result)

