# 01. Python 데이터 & 제어문

## 1. 세로로 출력하기

```python
number = int(input())


for i in range(1, number+1):

		print(i)
```





## 2. 거꾸로 세로로 출력하기

```python
number = 5

for i in range(number, -1, -1) :
    print(i)
    
    
while number > -1:
    print(number)
    number -= 1
```





## 3. N줄 덧셈 (SWEA #2025)

```python

total = 0

# 1. sum
sum(range(1, number+1))

# 2. for
for n in range(1, number+1):
    total += n 
    
total

# 3. while
total = 0
while number > 0:
    total += number
    number -= 1
total

# 4. 1 ~ n 자연수 총합 식
total = (number+1) * number / 2
int(total)
```

