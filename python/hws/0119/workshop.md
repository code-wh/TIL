# 1. 함수



## 1. List의 합 구하기

```python
def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        
    return total
```





## 2. Dictionary로 이루어진 List의 합 구하기

```python
def dict_list_sum(students):
    total = 0
    for student in students:
        total += student['age']
    return(student['age'])

dict_list_sum(students)
```





## 3. 2차원 List의 전체 합 구하기

```python
def all_list_sum(lists):
    
    total = 0
    for numbers in lists:
        for n in numbers:
            total += n
        return total

n_list = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
]

all_list_sum(n_list)
```

