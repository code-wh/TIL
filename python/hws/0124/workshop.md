# 05. 데이터 구조 및 활용

## 1. 평균 점수 구하기

``````python
def get_dict_avg(dict):
    total = 0
    scores = dict.values()
    for score in scores:
        total += score
    return total / len(scores)
``````



## 2. 혈액형 분류하기

``````python
def count_blood(list):
    A = list.count('A')
    B = list.count('B')
    AB = list.count('AB')
    O = list.count('O')
    return {'A' = A, 'B' = B, 'AB' = AB, 'O' = O}
``````

