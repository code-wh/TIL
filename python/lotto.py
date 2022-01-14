# ramdom 모듈을 꺼낸다

import random

# 1 ~ 45 까지의 숫자가 들어있는 통을 만든다.

# range (A, B): A부터 B까지의 정수
# A <= x < B ; B는 포함되지 않는게 중요 !  

numbers = range(1, 46)

# 통에서 6개를 랜덤으로 고른다
# sample: 무작위 비복원 추출
lucky = random.sample(numbers, 6) 

# 고른 숫자를 출력
print(lucky)