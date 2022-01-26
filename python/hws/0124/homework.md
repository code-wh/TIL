# 05. 데이터 구조 및 활용

## 1. 모음은 몇 개나 있을까?

``````python
def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total = 0
    for vowel in vowels:
        total += word.count(vowel)
	return total
``````



## 2. 문자열 조작

(4) .strip([chars])은 특정 문자를 지정하면 , 양쪽에서 해당 문자를 찾아 제거한다 . (O)

*특정 문자를 지정하지 않으면 오류가 발생한다* (X) => 지정하지 않을 시 **공백 제거**



## 3. 정사각형만 만들기

``````python
def only_square_area(list_x,list_y):
    area = []
    for x in list_x:
        for y in list_y:
            if x == y:
            	area.append(x*y)
    return area
``````



