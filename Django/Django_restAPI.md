# REST API



## HTTP

* HyperText Transfer Protocol
* HTML 문서와 같은 리소스들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
* 웹에서 이루어지는 모든 데이터 교환의 기초
  * 요청(request) : 클라이언트에 의해 전송되는 메세지
    * Method, Path, Version of the protocol, Headers
  * 응답(response) : 서버에서 응답으로 전송되는 메세지가
    * Version of the protocol, Status code, Status message, Headers
* 기본 특성
  * Stateless
  * Connectless
* 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함



## HTTP request methods

* 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄

  * GET, POST, PUT, DELETE

  ```
  # HTTP response status codes
  
  1. Informational responses (1xx)
  2. Succesful respondses (2xx)
  3. Redirection messages (3xx)
  4. Client error responses (4xx)
  5. Server error responses (5xx)
  ```



### URL, URN

* URI(Uniform Resource Identifier)
  *  일반적으로 URL은 URI와 같은 의미처럼 사용
  * URL(Uniform Resource Locator)
    * 통합 자원 위치
    * 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속
    * '웹 주소', '링크'라고도 불림
  *  URN(Uniform Resource Name)
    * 통합 자원 이름
    * URL과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역할
    * ex) ISBN(국제표준도서번호)



## API

* Application Programming Interface
* 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
  * CLI는 명령중, GUI는 그래픽(아이콘), API는 프로그래밍을 통해 특정한 기능 수행
* WEB API
  * 다른 서비스에 요청을 보내고 응답을 받기 위해 정의된 명세
  * 직접 개발보단 여러 Open API 활용
  * 응답 데이터 타입 : HTML, XML, JSON



## REST

* REpresentational State Transfer
* 네트워크 구조 원리의 모음
  * 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법
* REST의 자원과 주소의 지정 방법
  * 자원 : URI
  * 행위 : HTTP Method(GET, POST, PUT, DELETE)
  * 표현 : 결과물 - JSON으로 표현된 데이터를 제공

​	

### JSON

* JavaScript Object Notation

* JavaScript의 표기법을 따른 단순 문자열

* 특징

  * 사람이 읽거나 쓰기 쉽고 기계가 파싱(해석, 분석)하고 만들어내기 쉬움
  * 파이썬의 dictionary, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료 구조로 쉽게 변화할 수 있는 key-value 형태의 구조를 가지고 있음




### Django REST Framework

```bash
$ pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

```python
# articles/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
```

```python
# articles/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

@api_view()
def article_json_3(request):
	articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

```python
# test.py
import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/json-3/')
pprint(response.json())
# json file로 파싱해서 보여줌.
pprint(type(response.json()))
# list [{dict},{dict},{dict},]
pprint(response.json()[0])
# 데이터 접근 가능
```

