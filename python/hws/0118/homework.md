# 02. 데이터 & 제어문



## 1. Mutable & Immutable

```python
mutable => dict, set, list
immutable => tuple, range, string
```





## 2. 홀수만 담기

```python
list(range(1, 51))[::2]
```





## 3. Dictionary 만들기

```python
student = {
    '오른쪽친구' : 29
    '왼쪽친구' : 30
}
```





## 4. 반복문으로 네모 출력

```python
n, m = 5, 9

for _ in range(m):
    for _ in range(n):
        print('*', end='')
    print()
```





## 5. 조건 표현식

```python
temp = 36.5

msg = '입실 불가' if temp >= 37.5 else '입실 가능'
```





## 6. 평균 구하기

```python
scores = [80, 89, 99, 83]

# 1
print(sum(scores) / len(scroes))

# 2
total = 0
for score in scores:
    total += score
   
print(total / len(scores))
```

