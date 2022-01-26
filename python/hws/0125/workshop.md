# 06. 데이터 구조 및 활용

## 1. 무엇이 중복일까?

``````python
def duplicated_letters(word):
    results = []
    for char in word:
        if word.count(char) > 1 and char not in results:
            results.append(char)
    return results

print(duplicated_letters('apple'))
print(duplicated_letters('bananas'))
``````





## 2. 소대소대

``````python
# 1. enumerate 이용
def low_and_up(word):
    result=''
    for (idx, char) in enumerate(word):
        if idx % 2:
            result += char.upper()
        else:
            result += char.lower()
    return result

# 2. word[idx] 이용
def low_and_up(word):
    result=''
    for idx in range(len(word)):
        if idx % 2:
            result += word[idx].upper()
        else:
            result += word[idx].lower()
    return result

print(low_and_up('apple'))
print(low_and_up('banana'))
``````





## 3. 솔로 천국 만들기

``````python
# 1. 다음에 나오는 숫자와 비교
def lonely(list):
    result = [numbers[0]]
    for idx in range(1, len(numbers)-1):
        if numbers[idx] = numbers[idx+1]:
            result.append(numbers[idx+1])
	retrun result     
    
# 2. result에 있는 값들과 비교 
def lonely(list):
    result = [numbers[0]]
    for num in numbers:
        if result[-1] != num:
            result.append(num)
        return result
``````

