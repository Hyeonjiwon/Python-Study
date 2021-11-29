## 파이썬

### 네이밍 컨벤션(Naming Convention)

- 파이썬의 변수명 네이밍 컨벤션은 스네이크 케이스(Snake Case)를 따름
  > - 스네이크 케이스(Snake Case) : 각 단어를 밑줄(_)로 구분하여 표기하는 방법
  > ex) snake_case
  > - 카멜 케이스(Camel Case) : 단어별로 대소문자를 구별하여 표기하는 방법
  > ex) camelCase

- 소문자 변수명과 함수명이 기본 


### 타입 힌트

- 파이썬 버전 3.5 부터 사용 가능
- 타입 힌트를 사용할 경우 가독성이 좋아짐
- 버그 발생 확률을 줄일 수 있음 

```python
# 파라미터 a : 정수형, 반환 값 True 또는 False 
def fn(a: int) -> bool:
```
> mypy를 사용하여 타입 힌트에 오류가 없는지 자동으로 확인 가능
> pip install mypy
> mypy solution.py


### 리스트 컴프리헨션(List Comprehension)

- 기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문
- 파이썬 2.0부터 지원
- 람다 표현식에 map이나 filter를 섞어 사용하는 것 보다 가독성이 훨씬 높음

```python
# 홀수인 경우 2를 곱해 출력하는 리스트 컴프리헨션 
>> [n*2 for n in rnage(1, 10+1) if n%2 == 1]
[2, 6, 10, 14, 18]
```

- 버전 2.7 이후 딕셔너리 등이 가능하도록 추가
```python
a = {}
for key, value in original.items():
    a[key] = value

# 같은 구문
a = {key : value for key, value in original.items()}
```  

### 제너레이터 

- 루프의 반복 동작을 제어할 수 있는 루틴 형태
- **yield** 구문을 사용하여 제너레이터를 리턴, 제너레이터가 여기까지 실행 중이던 값을 내보낸다는 의미
- 중간 값을 리턴한 다음 함수는 종료되지 않고 계속해서 맨 끝에 도달할 때까지 실행 
- 다음 값을 생성하려면 next()로 추출

```python
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

# 100개의 값을 생성
g = get_natural_number()

for _ in range(0, 100):
    print(next(g))

# 여러 타입의 값을 하나의 함수에서 생성
def generator():
    yield 1
    yield 'string'
    yield True

g = generator()

>>> next(g)
1
>>> next(g)
'string'
>>> next(g)
True
``` 

### range

- 제너레이터 방식을 활용하는 대표적인 함수
- range는 range() 클래스를 리턴
- for문에 사용할 경우 내부적으로는 제너레이터의 next()를 호출하듯 매번 다음 숫자를 생성
- xrange() / 버전 3 이후 사라짐
- 인덱스 접근 시에는 바로 생성하도록 구현
  
```python
>>> list(range(5))
[0, 1, 2, 3, 4]

>>> range(5)
range(0, 5)

>>> type(range(5))
<class 'range'>

# 100만개 생성 방법
# a : 이미 생성된 값이 담겨 있음
a = [n for n in range(1000000)]

# b : 생성해야 한다는 조건만 존재, 메모리 점유율이 훨씬 작음
b = range(1000000)
```

### enumerate

- 여러 가지 자료형(list, set, tuple 등)을 인덱스를 포함한 enumerate 객체로 리턴
  
```python
a = ['a1', 'b1', 'c1']

for i, v in enumerate(a):
    print(i, v)

# 출력 결과
0, a1
1, b1
2, c1
```