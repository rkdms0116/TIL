# DB

---

### DB란?

- 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용
- 논리적으로 연관된 자료의 모음
- 구조화 검색과 생산의 효율화

⁕ <u>몇 개의 자료 파일</u>을 <u>조직적으로 통합</u>하여 자료 항목의 <u>중복을 없애</u>고 자료를 <u>구조화</u>하여 기억시켜 놓은 자료의 집합체



### DB로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성
- 데이터 일관성
- 데이터 독립성(물리적/논리적)
- 데이터 표준화
- 데이터 보안 유지



---

### RDB(Relational Database)

- 스키마(Schema) : DB의 자료의 구조, 표현 방법, 관계 등 명세를 기술
- 테이블(Table) : 열(column/field)와 행(recode/value)의 모델로 조직된 데이터 요소들의 집합
- 열(column) : **고유한** 데이터의 형식이 지정
- 행(row) : 실제 데이터가 저장되는 형태
- 기본키(primary key) : 각 행의 고유 값, **반드시 설정**해야 함



### RDBMS(Relational Database Management System)

ex) MySQL, SQLite, PostgreSQL, ORACLE, MS SQL



---

### SQL(Structed Query Language)

- 관계형 DB 관리시스템의 데이터 관리를 위해 설계
- DB의 스키마 생성 및 수정
- 자료의 검색 및 관리
- DB 객체 접근 조정 관리



### SQL 분류

|                         분류                          |               개념               |                        예시                         |
| :---------------------------------------------------: | :------------------------------: | :-------------------------------------------------: |
| DDL (Data Definition Language) <br />데이터 정의 언어 |  SQL 구조(Table, Schema)를 정의  |          - CREATE<br />- DROP<br />- ALTER          |
| DML(Data Manipulation Language)<br />데이터 조작 언어 | 데이터 저장, 조회, 수정, 삭제 등 | - INSERT<br />- SELECT<br />- UPDATE<br />- DELETE  |
|   DCL(Data Control Language)<br />데이터 제어 언어    |  사용자의 권한 제어를 위해 사용  | - GRANT<br />- REVOKE<br />- COMMIT<br />- ROLLBACK |



---

### 사용법

\# Option

```sqlite
sqlite> .headers on		# headers로 확인
sqlite> .mode column	# column도 확인하는 mode on
sqlite> .table 			# 생성되어있는 table 확인
```

\# Select : 저장된 데이터 확인

```sqlite
sqlite> SELECT * FROM examples;
```

```django
In[]: User.objects.all()
```



```sqlite
sqlite> SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자;
sqlite> SELECT id, name FROM classmates LIMIT 3 OFFSET 2; # 2번째에 있는 3개만 조회

sqlite> SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 WHERE 조건;
sqlite> SELECT rowid, name FROM classmates WHERE adress="서울";

sqlite> SELECT DISTINCT 컬럼 FROM 테이블이름;
sqlite> SELECT DISTINCT age FROM classmates;
```

```django
In[]: User.objects.get(id=100)
In[]: User.objects.all[:3]
```



🐾 `DISTINCT`의 경우 **<u>SELECT의 바로 뒤</u>**에서 사용 : 컬럼의 중복을 허용하지 않고 데이터 조회

\# Create Table : `classmates` 이름의 Table 생성

```sqlite
sqlite> CREATE TABLE classmates(
   ...> id INTEGER RTIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT
   ...> );
   # 만일 AUTOINCREMENT를 사용하면 key 값 재사용 X
```

```shell
In[]: User.objects.create(
	: first_name='길동',
	: last_name='홍'
	: )
```



\# schema 조회

```sqlite
sqlite> .schema classmate
```

\# Drop : Table 삭제

```sqlite
sqlite> DROP TABLE classmates;
```



\# Insert : 모든 열의 데이터가 있을 경우 컬럼을 따로 지정하지 않아도 됨!

```sqlite
sqlite> INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);
sqlite> INSERT INTO classmates (name, age) VALUES ('홍길동', 30);
sqlite> INSERT INTO classmates VALUES ('김철수', 27, '서울'), ('이지금', 26, '광주');
```

\# Delete : 테이블을 행에서 제거

```sqlite
sqlite> DELETE FROM 테이블이름 WHERE 조건;
sqlite> DELETE FROM classmates WHERE rowid = 5;
```

```djang
In[]: User.object.get(pk=5).delete()
```



\# Update : 기존 행의 데이터를 수정

```sqlite
sqlite> UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2, ... WHERE 조건;
sqlite> UPDATE classmates SET name='홍길동', adress='제주도' WHERE rowid=5;
```



---

### Aggregate Functions : SELECT 뒤에 사용

- COUNT : 그룹의 항목 수
- AVG : 값 집합의 평균 값
- MAX : 모든 최댓값
- MIN : 모든 최솟값
- SUM : 모든 합

---

### LIKE operator

- % : 0개 이상의 문자, 이 자리에 문자열이 <u>있을 수도, 없을 수도</u> 있다.
- _ : 임의의 단일 문자, **반드시** 이 자리에 <u>한 자리</u>의 문자가 존재

```sqlite
sqlite> SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴'
```

---

### ORDER BY clause

: 조회 결과 집합을 정렬

- ASC : 오름차순(default)
- DESC : 내림차순

```sqlite
sqlite> SELECT * FROM 테이블 ORDER BY 컬럼 ASC;
sqlite> SELECT * FROM 테이블 ORDER BY 컬럼1, 컬럼2 DESC;
```

---

### GROUP BY clause

: 문장에 WHERE 절이 있을 경우 **반드시 WHERE 절 뒤**에 작성

```sqlite
sqlite> SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 WHERE 조건 GROUP BY 컬럼1, 컬럼2 
```

---

### ALTER TABLE statement

- Table 이름 변경
- Table에 새로운 column 추가
- column 이름 수정

```sqlite
sqlite> ALTER TABLE table_name RENAME TO new_table_name;
sqlite> ALTER TABLE table_name ADD COLUMN 컬럼 데이터타입;

sqlite> RENAME COLUMN current_name To new_name;
```

```sqlite
sqlite> ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT '소제목';
```

<해결방법 2가지>

1. NOT NULL 설정 없이 추가
2. 기본 값(DEFAULT)설정

