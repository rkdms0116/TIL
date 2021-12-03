```bash
# 있으면 열고, 없으면 생성해서 열어줍니다.
$ sqlite3 tutorial.sqlite3


```

```sqlite
sqlite> .database
main: C:\Users\vwv15\Desktop\SSAFY\SQL\sql\tutorial.sqlite3 r/w
sqlite> .mode csv

# examples에 hellodb.csv 데이터를 넣음
sqlite> .import hellodb.csv examples
sqlite> .tables
examples
```

```
# 01_intro.sql
SELECT * FROM examples;
```

```sqlite
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232      

# header 정보가 보여짐
sqlite> .headers on
sqlite> SELECT * FROM examples;
id,first_name,last_name,age,country,phone     
1,"길동","홍",600,"충청도",010-2424-1232

# column 까지 보여줌
sqlite> .mode column
sqlite> SELECT * FROM examples;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------
1   길동          홍          600  충청도     
 010-2424-1232
```

```sqlite
# Table 생성
sqlite> CREATE TABLE classmates(
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );

# table 확인
sqlite> .tables
classmates  examples

# 스키마 확인
sqlite> .schema classmates
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT
);
```

```sqlite
# 테이블 삭제하기
# classmates 삭제되고 examples만 남는 결과

sqlite> DROP TABLE classmates;
sqlite> .tables
examples
```

```sqlite
# insert 해보기

sqlite> INSERT INTO classmates (name, age) VALUES ('홍길동', 23);  
sqlite> SELECT * FROM classmates
name  age  address
----  ---  -------
홍길동   23

sqlite> INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, 'seoul');
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   23
홍길동   30   seoul

# 모든 필드를 채워 넣을 때에는 굳이 넣지 않아도 됩니다.
sqlite> INSERT INTO classmates VALUES('홍길동', 40, '대전');
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   23
홍길동   30   seoul
홍길동   40   대전

# PRIMARYID 값을 SQL에서 자동으로 채워넣어주는 rowid
sqlite> SELECT rowid, * FROM classmates;      
rowid  name  age  address
-----  ----  ---  -------
1      홍길동   23
2      홍길동   30   seoul
3      홍길동   40   대전
```



```sqlite
# 삭제 후 다시 만들어보기
DROP TABLE classmates;

# INTEGER : PRIMARY KEY, 그 외에는 INT
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

.schema classmates
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

# 값 없이는 안들어감
sqlite> INSERT INTO classmates VALUES('홍길동', 30, '서울');
Error: table classmates has 4 columns but 3 values were supplied

# 올바른 방향
sqlite> INSERT INTO classmates VALUES(1, '홍길동', 30, '서울');
sqlite> SELECT * FROM classmates;
id  name  age  address
--  ----  ---  -------
1   홍길동   30   서울
```

```sqlite
DROP TABLE classmates;

CREATE TABLE classmates(
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

sqlite> INSERT INTO classmates VALUES
   ...> ('홍길동', 30, '서울'),
   ...> ('김철수', 30, '대전'),
   ...> ('이싸피', 26, '광주'),
   ...> ('박삼성', 29, '구미'),
   ...> ('최전자', 28, '부산');
   
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   30   서울
김철수   30   대전
이싸피   26   광주
박삼성   29   구미
최전자   28   부산

# classmates 테이블에서 id, name컬럼만 조회
sqlite> SELECT rowid, name FROM classmates;
rowid  name
-----  ----
1      홍길동
2      김철수
3      이싸피
4      박삼성
5      최전자

```

데이터 조회 및 필터링

```sqlite
# classmates 테이블에서 id가 5인 레코드를 삭제
sqlite> DELETE FROM classmates WHERE rowid=5;

# 데이터는 잘 삭제 되었는데 데이터를 다시 추가하면 rowid는 어떻게 될까?
# = 다시 rowid 5로 들어갑니다 => 재사용합니다 
INSERT INTO classmates VALUES ('최전자', 28, '부산');

```

UPDATE

```sqlite
# classmates 테이블에 id가 5인 레코드 수정
sqlite> UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
홍길동   30   서울
김철수   30   대전
이싸피   26   광주
박삼성   29   구미
홍길동   28   제주도
```



```sqlite
# 새로운 table 정의
★ 데이터에서 , 마지막에 저거 쓰지 않기!
sqlite> CREATE TABLE users (
   ...> first_name TEXT NOT NULL,
   ...> last_name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> country TEXT NOT NULL,
   ...> phone TEXT NOT NULL,
   ...> balance INT NOT NULL
   ...> );
   
sqlite> .mode csv
sqlite> .import users.csv users
sqlite> .tables
classmates  examples    users
sqlite> SELECT * FROM users;
와라락

### filter
# users 테이블에서 age가 30 이상인 유저의 모든 컬럼 확인
sqlite> SELECT * FROM users WHERE age >= 30;

# users 테이블에서 age가 30 이상인 유저의 first_name만 조회
sqlite> SELECT first_name FROM users WHERE age >= 30;

# users 테이블에서 age가 30 이상이고 성이 '김'인 유저의 나이와 last_name만 조회
sqlite> SELECT age,last_name FROM users WHERE age>=30 AND last_name='김';
```



```sqlite
# users table 안에 있는 레코드의 총 개수
sqlite> SELECT COUNT(*) FROM users;
COUNT(*)
1000

# 30살 이상인 사람들의 평균 나이
sqlite> SELECT AVG(age) FROM users WHERE age >=30;    
AVG(age)
35.1763285024155

# 계좌 잔액(balance)이 가장 높은 사람과 그 액수
sqlite> SELECT first_name, MAX(balance) FROM users;   
first_name,MAX(balance)
"순옥",1000000

# 나이가 30살 이상인 사람들의 평균 계좌 잔액
sqlite> SELECT AVG(balance) FROM users WHERE age >= 30;
AVG(balance)
153541.425120773
```

```sqlite
SELECT * FROM 테이블 WHERE 컬럼 LIKE '와일드카드패턴';
2% : 2로 시작
%2 : 2로 끝남
%2% : 2가 들어가있기만 하면 됩니다(처음,중간,끝)
_2% : 두번째가 2로 시작
1___ : 1로 시작하고 총 네자리
2_%_% : 2로 시작하고 적어도 3자리의 값
2__%

# USER table에서 나이가 20대인 사람만 조회
sqlite> SELECT * FROM users WHERE age LIKE '2_';      
first_name,last_name,age,country,phone,balance        
"서준","이",26,"충청북도",02-8601-7361,530

# USER table에서 지역 번호가 02인 사람만 조회
sqlite> SELECT * FROM users WHERE phone LIKE '02-%';  

# USER table에서 이름이 '준'으로 끝나는 사람
sqlite> SELECT * FROM users WHERE first_name LIKE "%준";

# USER table에서 phone 중간번호가 5114인 사람
sqlite> SELECT * FROM users WHERE phone LIKE '%-5114-%';
```

```sqlite
ORDER BY
SELECT * FROM 테이블 ORDER BY 컬럼 ASC;
SELECT * FROM 테이블 ORDER BY 컬럼1, 컬럼2, ... DESC;

# USER table에서 나이 오름차순으로 정렬하여 상위 10개만 조회
sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;

# 나이 순, 성 순으로 오름차순 정렬하여 상위 10개만 조회
sqlite> SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;

# 계좌 잔액순으로 내림차순 정렬하여 해당 유저의 성과 이름을 10개만 조회
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
```



```sqlite
GROUP BY
지정된 기준에 따라 행 세트를 그룹으로 결합/데이터 요약
SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;

AS를 이용하여 COUNT에 해당되는 컬럼 명을 바꿔서 조회할 수 있음

# users에서 각 성씨가 몇 명씩 있는지 조회한다면?
sqlite> SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
```



### 복습

```sqlite
Q. title과 content컬럼을 가진 articles라는 이름의 table을 새롭게 만들어봅니다.
sqlite> CREATE TABLE articles (
   ...> title TEXT NOT NULL,
   ...> content TEXT NOT NULL
   ...> );
sqlite> .tables
articles    classmates  examples    users

Q. articles 테이블에 값을 추가해보세요.
sqlite> INSERT INTO articles VALUES('1번제목','1번내용');
sqlite> SELECT * from articles;
title,content
"1번제목","1번내용"

```



```sqlite
ALTER TABLE

# 테이블 이름 변경
sqlite> ALTER TABLE articles RENAME TO news;
sqlite> .tables
classmates  examples    news        users

sqlite> ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
Error: Cannot add a NOT NULL column with default value NULL
테이블에 있던 기존 레코드들에는 새로 추가할 필드에 대한 정보가 없음
<해결방법>
1. NOT NULL 설정 없이 추가
2. 기본값(DEFAULT) 추가해주기

sqlite> ALTER TABLE news ADD COLUMN created_at TEXT;
sqlite> ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT '소제목';
```

```sqlite
# SQL_ORM

# sql모드 켬
$ sqlite3 db.sqlite3
SQLite version 3.36.0 2021-06-18 18:36:39
Enter ".help" for usage hints.
sqlite> .table
auth_group                  django_admin_log
auth_group_permissions      django_content_type
auth_permission             django_migrations
auth_user                   django_session
auth_user_groups            users_user
auth_user_user_permissions

sqlite> .mode csv
sqlite> .import users.csv users_user
sqlite> SELECT * FROM users_user;
sqlite> .schema users_user
CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
```

```sqlite
sqlite> .shell clear
sqlite> .exit

django_shell_plus
clear
exit

$ python manage.py shell_plus
```



| sql                                                          | <django_shell_plus>                                          |                           |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------- |
| $ sqlite3 db.sqlite3                                         | $ python manage.py shell_plus                                | 실행하기                  |
| SELECT * FROM users_user;                                    | User.objects.all()                                           | 모든 객체 확인            |
| INSERT INTO users_user VALUES(102,'길동','백',100,'경상북도','010-1234-5678',1000); | In []: User.objects.create(<br/>   ...: first_name='길동',<br/>   ...: last_name='홍',<br/>   ...: age=100,<br/>   ...: country='제주도',<br/>   ...: phone='010.1111.2222',<br/>   ...: balance=10000<br/>   ...: )<br/>Out[]: <User: User object (101)> | 새로운 객체 삽입          |
| # 확인<br />sqlite> SELECT * FROM users_user WHERE id=101;  <br/>id,first_name,last_name,age,country,phone,balance,101,"길동","홍",100,"제주도",010.1111.2222,10000<br />sqlite> SELECT * FROM users_user LIMIT 1 OFFSET 100;<br />sqlite> SELECT * FROM users_user LIMIT 2 OFFSET <br/>100;<br/>id,first_name,last_name,age,country,phone,balance<br/>101,"길동","홍",100,"제주도",010.1111.2222,10000<br />102,"길동","백",100,"경상북도",010-1234-5678,1000 | In [5]: User.objects.get(id=102)<br/>Out[5]: <User: User object (102)> | 객체 확인하기             |
| sqlite> UPDATE users_user SET first_name = "주호<br/>", last_name ="맹수" WHERE rowid = 101;<br/>sqlite> SELECT * FROM users_user WHERE id=101;  <br/>id,first_name,last_name,age,country,phone,balance<br/>101,"주호","맹수",100,"제주도",010.1111.2222,10000 | In [6]: user = User.objects.get(id=102)<br/><br/>In [7]: user.first_name = '정빈'<br/><br/>In [8]: user.first_name<br/>Out[8]: '정빈'<br/><br/>In [9]: user.save() | 업데이트 하기             |
| sqlite> DELETE FROM users_user WHERE id=101;                 | In [10]: user = User.objects.get(id=102)        <br/><br/>In [11]: user.delete()<br/>Out[11]: (1, {'users.User': 1})<br />User.objects.get(id=102).delete() | 정보 삭제하기             |
| sqlite> SELECT COUNT(*) FROM users_user;        <br/>COUNT(*)<br/>100 | In [12]: User.objects.count()<br/>Out[12]: 100               | 전체 유저의 수 조회       |
| sqlite> SELECT first_name FROM users_user WHERE <br/>age = 30;<br/>first_name<br/>"영환"<br/>"보람"<br/>"은영" | In [13]: print(User.objects.filter(age=30).values('first_name') )<br/><QuerySet [{'first_name': '영환'}, {'first_name': '보람'}, {'first_name': '은영'}]> | 30살 이상                 |
| sqlite> SELECT COUNT(*) FROM users_user WHERE age>=30;<br/>COUNT(*)<br/>43 | In [14]: User.objects.filter(age__gte = 30).count()<br/>Out[14]: 43 | 30살 이상인 사람의 인원수 |
| sqlite> SELECT COUNT(*) FROM users_user WHERE age=30 AND last_name='김';<br/>COUNT(*)<br/>1 | In [15]: User.objects.filter(age=30, last_name= '김').count()<br/>Out[15]: 1<br /><br />In [17]: User.objects.filter(age=30).filter(las <br/>    ...: t_name='김').count()<br/>Out[17]: 1 | 30살 이면서 김씨인 사람   |
| sqlite> SELECT AVG(age) FROM users_user;        <br/>AVG(age)<br/>28.23 | In [18]: User.objects.all().aggregate(Avg('age'))<br />Out[18]: {'age__avg': 28.23} |                           |
|                                                              |                                                              |                           |







