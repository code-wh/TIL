# 0117

## 1. Python 예약어
```python
import keyword
print(keyword.kwlist)

['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```





## 2. 실수 비교

```python
num1 = 0.1 * 3
num2 = 0.3

1. abs(num1 - num2) <= 1e-10  # 두 수의 차가 1e-10 이하

2. import sys
   abs(num1 - num2) <= sys.float_info.epsilon  # sys 모듈 이용

3. import math
   math.isclose(num1, num2)  # math 모듈 이용
```





## 3. 이스케이프 시퀀스

```python
(1) 줄바꿈: \n

(2) 탭: \t

(3) 백슬래시: \\
```





## 4. String Interpolation

```python
name = '철수'
print(f'안녕, {name}야')
```





## 5. 형 변환

```python
int('3.5') => 오류 발생
ValueError: invalid literal for int() with base 10: '3.5'
```





## 6. 네모 출력

```py
n , m = 5 , 9

print(('*'*n + '\n' ) * m)
```





## 7. 이스케이프 시퀀스 응용

```python
print('\"파일은 c:\\windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\''))
```





## 8. 근의 공식

```python
r1 = (-b + (b**2 - 4*a*c)**(1/2) / (2*a)
r2 = (-b - (b**2 - 4*a*c)**(1/2) / (2*a)
```

