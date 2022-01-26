# 06. 데이터 구조 및 활용

## 1. .sort()와  sorted()의 차이

.sort() : 내장함수 sorted()와 다르게 **원본 list를 변형**시키고, **None을 리턴**

``````python
lotto = [27, 45, 40, 34, 25, 17]

lotto.sort()  #  원본의 값이 변하고 None을 리턴
print(lotto) == [17, 25, 27, 34, 40, 45]
print(lotto.sort()) == None

sorted(lotto)  #  원본의 값이 변하지 않고 정렬된 list를 리턴
print(lotto) == [27, 45, 40, 34, 25, 17]
print(sorted(lotto)) == [17, 25, 27, 34, 40, 45]
``````





## 2. .extend()와 .append()의 차이

.append() : 리스트에 **값**을 추가 , 원본 변경

.extend() : 리스트에 **iterable값(list, range, tuple, string)** 추가, 원본 변경

``````python
drink = ['water', 'coffee', 'juice']

drink.append('beer') 
drink = ['water', 'coffee', 'juice', 'beer']  # 'beer' 통째로 들어감

drink.extend('beer')
drink = ['water', 'coffee', 'juice', 'b', 'e', 'e', 'r']  # 문자열을 순회해서 추가 
``````



## 3. 복사가 잘 된 건가?

``````python
a = [1, 2, 3, 4, 5]  # Global frame 안에 a라는 변수명을 가진 리스트 생성
b = a  # 마찬가지로 b라는 변수명을 가진 리스트를 생성하는데 a와 같은 객체 참조

a[2] = 5  # a = [1, 2, 5, 4, 5], 이때 b도 같은 객체를 참조하므로 b도 변경

print(id(a))
print(id(b))
=> a와 b의 주소값이 같다는 것을 알 수 있음. 따라서 둘은 같다고 볼 수 있다. 
``````
