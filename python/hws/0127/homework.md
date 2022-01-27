# 08. 객체 지향 프로그래밍

## 1. Circle 인스턴스 만들기

``````python
class Circle:
    pi = 3.14

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.pi * self.r * self.r

    def circumfernece(self):
        return 2 * self.pi * self.r

    def center(self):
        return (self.x, self.y)

circle_01 = Circle(3, 2, 4)

print(circle_01.area())  # 넓이
print(circle_01.circumfernece())  # 둘레

$ python a.py
28.259999999999998
18.84
``````



## 2. Dog과 Bird는 Animal이다

``````python
class Animal:
    """Master Class"""
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')


class Dog(Animal):
    """Sub Class"""

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    """Sub Class"""

    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
``````



## 3. 오류의 종류

- ZeroDivisionError: 0으로 나눴을 때 나타나는 오류
- NameError: 변수 이름이 틀렸거나 없는 변수를 사용할 때 나타나는 오류
- TypeError: 자료형이 맞지 않거나 함수 호출 규약이 틀렸을 때 나타나는 에러
- IndexError: 시퀀스 자료형에서 인덱싱 범위를 벗어날 때 나타나는 에러
- KeyError: 딕셔너리에 존재하지 않는 키로 접근할때 나타나는 에러
- ModuleNotFoundError: 모듈을 찾을 수 없을 때 나타나는 에러
- ImportError: 모듈을 가지오지 못할 때 나타나는 에러
  
