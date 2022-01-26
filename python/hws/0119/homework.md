# 03. 함수



## 1. Built-in 함수

```python
sum, print, max, min, bool, list, map, int, str, tuple, sorted

# [].append, [].sort()는 메서드
```





## 2. 정중앙 문자

```python
get_middle_char('ssafy')
get_middle_char('coding')

def get_middle_char(string):
    mid_idx = len(word) // 2
    
    if len(word) % 2: 
        return word[mid_idx]
    else:  
        return word[mid_idx-1:mid_idx+1]
    
```





## 3. 위치 인자와 키워드 인자

```python
def ssafy(name, location='서울'):
	print(f'{name}의 지역은 {location} 입니다.')
    
(4) 키워드 인자가 위치 인자보다 앞에 오면 안됨
```





## 4. 나의 반환값은

```python
None
# return을 안했기 때문에
```





## 5. 가변 인자 리스트

```python
def my_avg(*scores)):
    return sum(scores) / len(scores)
```





