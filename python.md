# escape sequence

```
\n : 줄바꿈
\t : 탭
\r : 캐리지리턴
\0 : 널(Null)
\\ : '\'출력
\' : ' 출력
\" : " 출력 
```



# 연산자 우선 순위

```python
#01 ()
#02 Slicing
#03 Indexing
#04 **
#05 단항 연산자(+, -) : 부호 
-2**6 == -64
#06 산술 연산자(*, /, %) : 곱셈, 나눗셈, 나눈 뒤 나머지
#07 산술 연산자(+, -)
#08 비교 연산자(>, < 등), in, is
#09 not
#10 and
#11 or
```



# Container

* sequence : ordered data

  > ex) list, tuple, range, string, binary

* non-sequence : unordered data

  > ex) set, dictionary



# List

* 서로 다른 type의 data를 저장할 수 있다.

  ```python
  list_test = [[1,2],[3,4]]
  list_test[0][1] == 2	# List 안에 List 가능
  ```

# Tuple

* immutable(수정 불가능)한 sequence로 인덱스로 접근

* 하나의 항목으로 이루어진 튜플 생성 시 값 뒤에 쉼표를 붙여야 한다. 

  ```python
  I_want_Tuple = (1,)
  ```



# Set

```python
Set_fir = {1, 2, 3}
Set_sec = {3, 4, 5}
Set_fir - set_sec == {1, 2}		# 차집합
Set_fir | Set_sec == {1, 2, 3, 4, 5} 	# 합집합
Set_fir & Set_sec == {3}
```



# Dictionary



# Syntax Error

```html
Invalid syntax : 
assign to literal : 
EOL(End of Line) :
EOF(End of File) :

```



# Exception

```html
ZeroDivisionError : 0으로 나누고자 할 때 발생
NameError : namespace 상에 이름이 없는 경우

```

