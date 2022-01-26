# Python 02. 데이터 & 제어문



## 1. 간단한 N의 약수

```python
N = 10

for i in range(1, N+1):
    if N & i == 0:
        print(i, end='')
```





## 2. 중간값 찾기

```python
numbers = [85, 72, ....]

numbers.sort()

center_inx = len(numbers) // 2

numbers[center_idx]
```





## 3. 계단 만들기

```python
number = int(input('자연수 입력 : '))

for i in range(1, number+1):
    for j in range(1, i+1):
        print(j, end='')
    print()
    
```



