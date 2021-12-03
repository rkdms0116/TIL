# Django



## Django 실행 환경 맞춰놓기

```bash
# 가상환경 생성 (run library module as a script (terminates option list))
$ python -m venv venv

# venv가 있는 폴더에서 활성화 하고 들어가기
$ source venv/Scripts/activate

# requirements에 있는 환경 맞추기
$ pip install -r requirements.txt

# 현재 나의 환경을 파일에 저장하기
$ pip freeze > requirements.txt

# 설치되어있는 list 목록 확인하기
$ pip list

# README 및 git ignore 파일 만들기
$ touch README.md .gitignore

# Django/ Django-extensions 설치
$ pip install django django_extensions
```



## Django 기본 파일 설정

```bash
# 현재 폴더 안에(.) 'crud' 이름으로 startproject 생성
$ django-admin startproject crud .

# 밑줄 쳐진 서버(http://127.0.0.1:8000/)에 `ctrl`+`클릭` -> 장고 서버가 열림
$ python manage.py runserver

# startapp 'articles' 이름으로 어플리케이션 생성
$ python manage.py startapp articles

# startapp 'accounts' 이름으로 계정 관리 어플리케이션 생성
$ python manage.py startapp accounts

# templates 폴더 생성
$ mkdir templates

# templates 폴더로 이동
$ cd templates

# templates 폴더에 base.html 파일 생성
$ touch base.html
```



```bash
# 폴더 bash에서 빠르게 적용하기
$ cd articles

$ touch urls.py forms.py

$ mkdir -p templates/articles

$ cd templates/articles/

$ touch form.html index.html detail.html
```





```html
# templates/base.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% block content %}
    
    {% endblock content %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
</body>
</html>
```



```python
# crud/settings.py

# 생성한 어플리케이션 출생신고
INSTALLED_APPS = [
    'articles',
    'accounts',
    ...
]

# base.html 등록 
TEMPLATES = [
    {...
        'DIRS': [BASE_DIR/'templates'],
     ...
    }
]

# 언어, 시간 설정
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'


# 정적 파일 경로 지정
STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# MEDIA 파일 경로
MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

# Custom User
AUTH_USER_MODEL = 'accounts.User'
```



```python
# crud/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```



```python
# ariticles/urls.py (urls.py 파일 생성)

from django.urls import path
from . import views

app_name = 'articles'

# articles/ + 
urlpatterns = [
    path('', views.index, name='index'),
]
```



```python
# articles/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'articles/index.html')
```



```python
# articles/templates/articles/index.html
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <hr>
{% endblock content %}
```



## Django Model

* 데이터베이스(DB)
  * 체계화된 데이터의 모임
* 쿼리(Query)
  * 데이터를 조회하기 위한 명령어
  * 'Query를 날린다' = 'DB를 조작한다'
* 스키마(Schema)
  * 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조(strucure)
* 테이블(Table)
  * 열(column) : 필드(field) or 속성
  * 행(row) : 레코드(record) or 튜플

```python
# articles/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # object를 사람이 읽을 수 있는 문자열로 return
    def __str__(self):
        return self.title
```



```bash
# model을 변경할 때 새로운 마이그레이션을 만들 때 사용
$ python manage.py makemigrations

# 마이그레이션을 DB에 반영하기 위해 사용
$ python manage.py migrate
```



## Admin 생성

```bash
# Admin 계정 생성
$ python manage.py createsuperuser
```



```python
# articles/admin.py

from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    # list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    list_display = ['pk', 'title', 'content', 'created_at', 'updated_at']

admin.site.register(Article, ArticleAdmin)
```



## Form 생성

```python
# articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
```

