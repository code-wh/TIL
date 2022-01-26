# 07. 객체 지향 프로그래밍



## 1. Type Class

숫자 자료형, 리스트, 딕셔너리, 셋, 문자열, 튜플



## 2. Magic Method

``````python
__init__ : 초기화 ; 객체가 만들어질 때 자동으로 호출되어서 객체의 성질 정해줌
__del__: 소멸자 ; 리소스 해제 등의 종료 작업
__str__: 클래스 자체의 내용을 출력하고 싶을때 형식을 지정하는 메서드
__repr__: 어떤 객체의 출력될 수 있는 표현을 문자열의 형태로 반환
``````



## 3. Instance Method

``````python
.get(key): key의 value 값을 가져옴
.append(): list에 값 추가
.strip(): 양옆의 문자 제거
``````



## 4. Module Import

``````python
from __init__ import __fibo__ as __repr__

recursion(4)