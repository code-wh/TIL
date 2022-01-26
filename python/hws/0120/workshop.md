# 04. 함수

## 1. 숫자의 의미

```python
def get_secret_word(number):
    
    for number in numbers:
        
    return number

get_secret_word([83, 115, 65, 102, 89])
```





## 2. 내 이름은 몇일까?

```python
def get_secret_number(word):
    total = 0
    for char in word:
        total += ord(char)
    return total

get_secret_number('tom')
```





## 3. 강한 이름

```python
def get_strong_word(word1, word2):
    total1 = get_strong_word(word1)
    total2 = get_strong_word(word2)
    
    return word1 if total1 > total2 else word2
    
get_strong_word('z', 'a')
get_strong_word('tom', 'john')
```





