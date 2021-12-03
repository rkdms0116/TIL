## Static file 구성

1. `CRUD` \ `settings.py`\>INSTALLED_APPS = [ ... , 'django.contrib.staticfiles', ] 확인 => 기본적으로 포함되어 있음
2. `CRUD`\ `settings.py`\ STATIC_URL 정의 => 기본적으로 포함되어 있음



## 정적 파일 사용하기

1. 파일 경로 : `articles`\ <u>`static`\\`articles`</u> 생성 후 `파일`

2. `articles`\\`templates`\\`acticles`\\`원하는파일.html` 에 

   ```
   {% load static %}
   
   <img src="{% static 'articles/다운로드.jpg' %}" alt="smaple_image">
   ```

---

1. `CRUD`\\ `settings.py`\\

   ```python
   STATIC_URL = '/static/'		# '/'으로 끝남‼
   STATICFILES_DIRS = [
        BASE_DIR/'static'
   ]
   ```

2. <u>`static`\\`images`</u> 에 파일 추가

   ```
   {% load static %}
   
   <img src="{% static 'images/sample2.jpg' %}" alt="image_test">
   ```




## 이미지 업로드(사용자가 웹에서 업로드)

1. `CRUD` \\`settings.py`

   ```python
   MEDIA_ROOT = BASE_DIR / 'media'
   MEDIA_URL = '/media/'		# '/'으로 끝남‼
   ```

   경로 지정만 해주면 사용자가 파일을 업로드 하면 자동으로 파일 생성

   MEDIA_ROOT와 STATIC_ROOT는 다른 경로로 지정

   MEDIA_URL와 STATIC_URL은 다른 경로로 지정

2. `articles` \\`models.py`

   ```python
   from django.db import models
   
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
       image = models.ImageField(blank=True, upload_to='images/')
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

   blank=True : 이미지 필드에 빈 값(빈 문자열)이 허용 

   upload_to : 필수X

   ※ null : DB, form에서 빈 값을 허용하려면 blank=True

   ​	문자열 기반 필드에서 <u>NULL은 지양</u>

3. ⁂`CRUD` \\`urls.py` 에 추가 **(MEDIA_URL/MEDIA_ROOT 설정 우선)**

   google에 'django static files' 검색

   ```python
   from django.conf import settings
   from django.conf.urls.static import static
   
   urlpatterns = [
       # ... the rest of your URLconf goes here ...
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

   $ pip install Pillow	# image를 makemigrations하기 위해서 Pillow 설치

   $ pip freeze > requirements.txt 	#업데이트

   $ python manage.py makemigrations		# model class 변경한 것에 기반한 새로운 설계도 생성

   $ python manage.py migrate						# DB에 반영

5. `articles`\\`templates` \\`articles`\\ `creat.html`

   ```html
   <form action="" method="POST" enctype="multipart/form-data">
   ```

   **form에 enctype 속성 지정**(인코딩 type)

6. `articles` \\`views.py`

   ```python
   def create(request):
       if request.method == 'POST':
           form = ArticleForm(request.POST, request.FILES)
           if form.is_valid():
               article = form.save()
               return redirect('articles:index')
       else:
           form = ArticleForm()
       context = {
           'form': form,
       }
       return render(request, 'articles/create.html', context)
   ```

   form = ArticleForm()에 <u>**request.FILES**</u> 추가

7. 기타

   ```
   <input type="file" accept=".doc,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document">
   
   <input type="file" accept="image/*,.pdf">
   # audio/*는 "모든 오디오 파일"
   # video/*는 "모든 비디오 파일"
   # image/*는 "모든 이미지 파일"
   ```

   실제 파일 위치 : MEDIA_ROOT/images

   DB에 저장되는 파일 경로 : `media`>`images`

   

   이미지를 출력할 때,

   ```html
   {% for article in articles %}
   	{% if article.image %}
   		<img src="{{ article.image.url }}" alt="{{ article.image }}">
   	{% else %}
   		<p>업로드된 이미지가 없습니다!</p>
   	{% endif %}
   	<p>글 번호 : {{ article.pk }}</p>
   	<p>글 제목 : {{ article.title }}</p>
   	<p>글 내용 : {{ article.content }}</p>
   	<hr>
   {% endfor %}
   ```



## 이미지 업로드(수정할 경우/UPDATE)

1. `articles`\\`templates` \\`articles`\\`update.html`

   ```html
     <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
   ```

   `create.html`과 동일하게 **form에 enctype 속성 지정**

   

2. `articles`\\`views.py`

   ```python
   @require_http_methods(['GET', 'POST'])
   def update(request, pk):
       article = get_object_or_404(Article, pk=pk)
       if request.method == 'POST':
           form = ArticleForm(request.POST, request.FILES, instance=article)
           if form.is_valid():
               form.save()
               return redirect('articles:detail', article.pk)
       else:
           form = ArticleForm(instance=article)
       context = {
           'article': article,
           'form': form,
       }
       return render(request, 'articles/update.html', context)
   ```

    ※ 순서 주의 form = ArticleForm(request.POST, request.FILES, instance=article) 

3. DETAIL 문제 해결

   ```html
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3>
     {% if article.image %}
       <img src="{{ article.image.url }}" alt="{{ article.image }}">
     {% else %}
     	# 대체 이미지는 static에 이미 넣어둠 (static/image)
       <img src="{% static 'images/default.jpg' %}" alt="default image">
     {% endif %}
   ```

   

## 이미지 업로드(2번추가_1)

1. 문자열 경로 지정 방식

   `articles` \\`models.py`

   ```python
   class Article(models.Model):
   	...
   	image = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
   	...
   ```

   `media`\`2021`\`09`\`08` 에 파일 저장됨

   

2. 함수 호출 방식

   ```python
   def articles_image_path(instance, filename):
   	# MEDIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
       return f'user_{instance.pk}/{filename}'
       
   class Article(models.Model):
   	 image = models.ImageField(upload_to=articles_image_path, blank=True)
   ```



## Image resizing(2번추가_2)

※ 참고 : django-imagekit

$ pip install django-imagekit

$ pip freeze > requirements.txt

`CRUD` \\`settings.py`

```python
INSTALLED_APPS = [
 ...
 'imagekit',
 ...
]
```



`articles` \\`models.py`

1. 사진을 자른 상태로 저장하기

   ```python
   from imagekit.models import ProcessedImageField, ImageSpecField
   from imagekit.processors import ResizeToFill
   
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
       # image = models.ImageField(upload_to='images/', blank=True)
       # image = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
       # image = models.ImageField(upload_to=articles_image_path, blank=True)
       image = ProcessedImageField(
           upload_to='thumbnails/',
           processors=[ResizeToFill(100, 50)],	# 100*50 size로 잘라버리기
           format='JPEG',
           options={'quality': 60}	# 60%
       )
   ```

   $ makemigrations/migrate

   

2. 원본을 따로 저장하고 사진을 잘라서 저장하기

   ```python
   	# 원본 파일은 origin에 저장
   	image = models.ImageField(upload_to='origins/', blank=True)
       image_thumbnail = ImageSpecField(
           source='image',
           processors=[ResizeToFill(100, 50)],
           format='JPEG',
           options={'quality': 90},
       )
   ```

   그 후 출력되는 `detail.html` 수정

   ```html
     {% if article.image %}
       <img src="{{ article.image_thumbnail.url }}" alt="{{ article.image_thumbnail }}">
     {% else %}
       <img src="{% static 'images/default.jpg' %}" alt="default image">
     {% endif %}
   ```

   



※  배포할 때

`CRUD` > `settings.py`>STATIC_ROOT = BASE_DIR / 'staticfiles'

$ python manage.py collectstatic

`CRUD` > `settings.py`>DEBUG =True이면 STATIC_ROOT 적용되지 않음