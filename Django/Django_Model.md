$ pip install ipython
: 컬러를 입히기 위함

$ pip install django-extensions
: 장고 익스텐션 설치

`CRUD`\\`settings` 

```I
INSTALLED_APPS = [
	'django_extensions',
]
```

$ pip install ipython
: 쥬피터 노트북처럼 만들어주겠다.

$ python -i
: python shell 활성화

$ python manage.py shell_plus
shell보다 큰 + 상황 킴

---

### 방법 1

In [1]: article = Article()
: 인스턴스 객체 생성

In [2]: article
Out[2]: <Article: Article object (None)>: 지금 비어있음

In [3]: article.title = 'first'

In [4]: article.content = 'django!'

In [5]: Article.objects.all()
Out[5]: <QuerySet []>

In [6]: article.save()
: 이제 저장됨
In [7]: Article.objects.all()
Out[7]: <QuerySet [<Article: Article object (1)>]>

```db.sqlite3 -우마우스 -OpenDataBase- > 들어가서 확인 가능```

*** 확인
In [8]: article.title
Out[8]: 'first'

In [9]: article.content
Out[9]: 'django!'

In [10]: article.id
Out[10]: 1

In [11]: article.pk
Out[11]: 1		#숏컷 기능

In [13]: article.create_at
Out[13]: datetime.datetime(2021, 9, 1, 5, 10, 43, 796605, tzinfo=<UTC>)

***

### 방법2

In [14]: article = Article(title = 'second', content = 'django!!')

In [15]: article
Out[15]: <Article: Article object (None)>
None : DB에 저장이 안되어있음

In [16]: article.save()

In [17]: article
Out[17]: <Article: Article object (2)>

---

### 방법3

In [19]: Article.objects.create(title='third', content='django')
Out[19]: <Article: Article object (3)>
: 인스턴스의 생성과 저장을 한큐에 끝낼 수 있음

    # <Article: Article object (3)>이였던 출력방식 변경
    def __str__(self):
        return self.title
    ★저장 후

In [21]: exit()