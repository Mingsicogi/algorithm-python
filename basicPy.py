

a=1000
print(a)


a = 7
b = 3

print(a/b) #나누기
print(a%b) #나머지
print(a//b) # 몫

print(5 ** 3) # 거듭제곱
print(2 ** 0.50) # 제곱근


##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################


# list comprihansion
array = [i for i in range(20) if i % 2 == 1]
print(array)

# reverse index
print(array[-1])

# initialize by zero
array = [0] * 20
print(array)

# list comprihansion best use case
n = 4
m = 3

print([0] * m)

array = [[0] * m for _ in range(n)]
print(array)

# under score(_) : 파이썬에서는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할때 자주 사용함
sum = 0
for i in range(10) :
    sum += i
print(sum)

for _ in range(10) :
    print("hello world~!")


# list extra method
array = [i for i in range(10)]
array.reverse() # O(N)
print(array)

array.append(50) # O(1)
print(array)

array.sort() # O(NlogN)
print(array)

array.sort(reverse=True) # O(NlogN)
print(array)

array.insert(2, 10) # O(N)
print(array)

array.insert(2, 10)
print(array)
print(array.count(10)) # O(N)

array.remove(10) # O(N), 값이 10인 데이터 삭제. 한개씩 삭제됨
print(array)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)