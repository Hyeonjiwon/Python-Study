
- iterable : 자신의 멤버를 한 번에 하나씩 리턴할 수 있는 객체
  (list, str, tuple, dict)

- sequence : int 타입 인덱스를 통해 원소에 접근할 수 있는 iterable, iterable 객체의 하위 카테고리(list, str, tuple)


## list

- list 생성 

```python
a = []
a = list()

b= [1, 2, 3, 4, 5]
c = ['Hi', 'Hello', 'Python']
d = [1, 2, 'AA', 'BB']
```

- 인덱싱

```python
a = [1, 2, 3]
b = [1, 2, ['a', 'b']]

a[0] # 1
a[-1] # -1

b[-1] # ['a', 'b']
b[-1][0] # 'a'
```

- 슬라이싱

```python
a = [1, 2, 3, 4, 5]
a[0:2] # [1, 2]
a[:3] # [1, 2, 3]
a[2:] # [3, 4, 5]

s = "abcde"
s[0:2] # 'ab'
```

- 연산 

```python
a = [1, 2]
b = [3, 4, 5]

## 더하기(+)
a + b # [1, 2, 3, 4, 5]

## 반복하기(*)
a * 3 # [1, 2, 1, 2, 1, 2]

## 리스트 길이 
len(a) # 2
```

- 값 수정 삭제
  
```python
## 수정
a = [1, 2, 3, 4, 5]
a[2] = 4 
a # [1, 2, 4, 4, 5]

## 삭제
del a[2]
a # [1, 2, 4, 5]

del a[:3] 
a# [5]
```

```python
del 객체 
```


## 리스트 관련 함수

- 요소 추가 append()

```python
a = [1, 2, 3]
a.append(4)
a # [1, 2, 3, 4]

a.append("AAA")
a.append([5, 6])
a # [1, 2, 3, 4, 'AAA', [5, 6]]
```

- 정렬 sort()
  
  리스트를 제자리에서(in-place) 수정하는 내장 메서드 (None 반환)

```python
a = [1, 3, 5, 2, 4]

# a의 내용을 변경하여 정렬
a.sort()
a # [1, 2, 3, 4, 5]

a.sort(reverse=True)
a # [5, 4, 3, 2, 1]

a = ['a', 'c', 'b']
a.sort()
a # ['a', 'b', 'c']

a.sort(reverse=True) 
a # ['c', 'b', 'a']

sort_a = a.sort()
sort_a # None
```


> **sorted()**
>> iterable로부터 정렬된 새로운 리스트를 생성
>  ```python
>>> a = sorted([5, 2, 3, 1, 4])
>>> a
> [1, 2, 3, 4, 5]
>  ```


- 뒤집기 reverse()
  
  리스트를 그대로 거꾸로 뒤집음, 순서 정렬 후 뒤집기 x 

```python
a = [1, 3, 5, 2]

a.reverse() 
a # [2, 5, 3, 1] 
```


- 위치 반환 index()
  
  index(x) : x의 인덱스를 반환
  
```python
a = [1, 2, 3]
a.index(1) 
a # 0
```


- 요소 삽입 insert()
  
  index(a, b) : a번째 위치에 b 삽입
  
```python
a = [1, 2, 3]
a.insert(0, 6) 
a # [6, 1, 2, 3]
```


- 요소 제거 remove()
  
  remove(x) : 첫 번째로 나오는 x 삭제. 특정 값 삭제
  
```python
a = [1, 1, 2, 3]
a.remove(1) 
a # [1, 2, 3]
```


- 요소 꺼내기 pop()
  
  맨 마지막 요소를 꺼내고 그 요소는 삭제 
  
```python
a = [1, 2, 3, 4, 5]
a.pop() # 5
a # [1, 2, 3, 4]

## 특정 인덱스 삭제
a.pop(3) # 4
a # [1, 2, 3]
```


- 요소 개수 세기 count()
  
  count(x) : 리스트 안 x의 개수 반환
  
```python
a = [1, 1, 1, 2, 3]
a.count(1) # 3
```


- 리스트 확장 extent()
  
  extent(x) : x는 리스트만
  
```python
a = [1, 2, 3]
a.extend([4, 5])
a # [1, 2, 3, 4, 5]
```


> 리스트가 비어 있는지 확인하는 방법
>  ```python
> if not seq: # 리스트가 비어 있으면 True
> if seq:     # 리스트가 비어있지 않으면 True
>  ```

- 최대 최소 구하기 

```python
a = [1, 2, 3, 4, 5]

min(a) # 1
max(a) # 5
```

- 합계 구하기 
```python
a = [1, 2, 3, 4, 5]

sum(a) # 15
```

## 리스트 컴프리헨션(list comprehension)

```python
>>> a = [i for i in range(10)]
>>> a 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> b = list(i for i in range(10))
>>> b 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> a = [i for i in range(10) if i%2 == 0]
>>> a
[0, 2, 4, 6, 8]

>>> a = [j * i for j in range(2,9)
              for i in range(1, 10)]
```


## 리스트에 map 사용하기 

- map은 리스트의 요소를 지정된 함수로 처리해주는 함수
- 새 리스트 생성, 원본 리스트 변경 x 

> list(map(함수, 리스트))
> 
> tuple(map(함수, tuple))

```python
>>> a = [1.2, 2.5, 3.7, 4.6]
>>> a = list(map(int, a))
>>> a
[1, 2, 3, 4]

>>> a = [1, 2, 3]
>>> a = list(map(str, a))
>>> a
['1', '2', '3']
```

- 컴프리헨션과 맵을 사용해 푼 문제 
```python
def solution(mylist):
    answer = [len(i) for i in mylist]
    return answer
```

```python
def solution(mylist):
    return list(map(len, mylist))
```

- input().split()과 map
  
```python
>>> a = map(int, input().split())
1 2 3
>>> a
<map object at 0x0000019A1647BA90>
>>> list(a)
[1, 2, 3]
```