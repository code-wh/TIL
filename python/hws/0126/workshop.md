# 07. 객체 지향 프로그래밍

## 1. PiP

``````bash
$ pip install faker
(1) 무엇을 위한 명령 : Faker라는 파이썬 패키지를 설치시키는 명령어
(2) 실행은 어디서: git bash 에서
``````



## 2. Basic Usages

``````python
from faker import faker  # 1 페이커에서 패키지를 가져오기 위한 코드
fake = Faker()           # 2 Faker는 클래스, fake는 인스턴스 이다 
fake.name()              # 3 name()은 fake의 메서드 이다.
``````



## 3. Localization

``````python
class Faker():
    def __init__((en_US), ('ko_KR')):
        pass
``````



## 4. Seeding the Generator

``````python
from faker import Faker
fake = Faker()
fake.name()

import random

random.random()
random.random()

random.seed(7777)
random.random()

random.seed(7777)
random.random()

fake = Faker('ko_KR')
Faker.seed(4321)

print(fake.name())  # 1 : 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())  # 2 : 이지후 

fake = Faker('ko_KR')
fake.seed_instance(4321)

print(fake.name())  # 1 : 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())  # 2 : 김광수

seed(): 난수 알고리즘을 실행하기 위해 쓰는 수
``````

