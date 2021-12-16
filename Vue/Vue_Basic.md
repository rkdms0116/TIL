# Basic Syntax of Vue.js

### Vue



##### Vue instance

* Vue Instance === Vue Component

```javascript
const app = new Vue ({
	el: '#app',
	data: {
    	message: 'Hello~',
	},
    methods: {
        greeting: function() {
            console.log('Hi :)')
        }
    },
    
})
```

##### option/DOM - 'el'

* Vue 인스턴스에 **마운트**할 기존 DOM 엘리먼트가 필요
* CSS 선택자 문자열 혹은 HTML Element로 작성
* new를 이용한 인스턴스 생성 때만 사용

##### option/Data - 'data'

* Vue의 인스턴스의 데이터 객체

* Vue template에서 interpolation을 통해 접근 가능

* v-bind, v-on과 같은 directive에서도 사용 가능

* Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능

  ❗주의

  화살표 함수를 'data'에서 사용하면 안 됨

  화살표 함수가 부모 컨텍스트를 바인딩하기 때문에, 'this'는 예상과 달리 Vue 인스턴스를 가리키지 않음

##### options/Data - 'methods'

* Vue의 인스턴스에 추가할 메서드

* Vue template에서 interpolation을 통해 접근 가능

* v-on과 같은 directive에서도 사용 가능

* Vue 객체 내 다른 함수에서 this 키워드를 통해 접근 가능

  ❗주의

  화살표 함수를 메서드를 정의하는데에 사용하면 안 됨

  화살표 함수가 부모 컨텍스트를 바인딩하기 때문에, 'this'는 Vue 인스턴스가 아니며 'this.a'는 정의되지 않음

##### options/Data = 'computed'

* 데이터를 기반으로 하는 계산된 속성
* 함수의 형태로 정의하지만 함수가 아닌 함수의 반환 값이 바인딩 됨
* 종속된 데이터에 따라 저장(캐싱)됨
* **종속된 데이터가 변경될 때만 함수를 실행**
* 반드시 반환 값이 있어야 함

##### options/Data - 'watch'

* 데이터를 감시
* 데이터에 변화가 일어났을 때 실행되는 함수

---

##### computed & methods

* computed 대신 methods에 함수를 정의할 수 있음 => 결과에 대해 두 가지 접근 방식은 동일
* 차이점 
  * computed : 종속된 대상이 변경되지 않는 한 함수를 여러 번 호출해도 다시 계산하지 않음, 단, 종속 대상을 따라 저장(캐싱)됨
  * methods : 호출할 때마다 렌더링을 다시하므로 함수를 실행

##### computed & watch

* 데이터를 감시
* 차이점
  * **computed** 
    * 특정 데이터를 직접적으로 사용/가공하여 다른 값으로 만들 때 사용
    * 속성은 계산해야 하는 목표 데이터를 정의하는 방식
    * '선언형 프로그래밍' 방식 : "계산해야 하는 목표 데이터를 정의"
  * **watch** 
    * 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야 할 때 주로 사용
    * 감시할 데이터를 지정하고, 그 데이터가 바뀌면 <u>특정 함수를 실행</u>하는 방식
    * '명령형 프로그래밍'방식 : "데이터가 바뀌면 특정 함수를 실행"

##### this

* Vue 함수 객체 내에서 vue 인스턴스를 가리킴

  ❗화살표 함수를 사용하면 안되는 경우

  1. data
  2. method 정의

---

##### Options/Assets - 'filter'

* 텍스트 형식화를 적용할 수 있는 필터
* interpolation 혹은 v-bind를 이용할 떄 사용 가능
* 필터는 자바스크립트 표현식 마지막에 `|` 와 함께 추가되어야 함





# Template Syntax

1. Interpolation
2. Directive

##### Interpolation

1. Text

   ```javascript
   <span>메세지 : {{msg}}</span>

2. Raw HTML

   ```javascript
   <span v-html="rawHtml"></span>
   ```

3. Attributes

   ```javascript
   <div v-bind:id="dynamicId"></div>
   ```

4. JS 표현식

   ```javascript
   {{ number + 1 }}
   {{ message.split('').reverse().join('') }}
   ```

##### Directive

* `v-접두사`가 있는 특수 속성
* 속성 값은 단일 JS 표현식이 됨(v-for는 예외)
* 표현식의 값이 변경될 떄 반응적으로 DOM에 적용하는 역할을 함

v-text

* 엘리먼트의 textContent를 업데이트
* 내부적으로 interpolation 문법이 v-text로 컴파일 됨

v-html

* 엘리먼트의 innerHTML을 업데이트
* XSS 공격에 취약할 수 있음
* 임의로 사용자로부터 입력받은 내용은 v-html에 **절대 사용 금지**

v-show

* 조건부 렌더링 중 하나
* 엘리먼트는 항상 렌더링 되고 DOM에 남아있음
* 단순히 엘리먼트에 display CSS 속성을 토글하는 것

v-if, v-else-if, v-else

* 조건부 렌더링 중 하나
* 조건에 따라 블록을 렌더링
* directive의 표현식이 true일 때만 렌더링
* 엘리먼트 및 포함된 directive는 토글하는 동안 삭제되고 다시 작성됨

v-for

* 원본 데이터를 기반으로 엘리먼트 또는 템플릿 블록을 여러번 렌더링
* item in items 구문 사용
* item 위치의 변수를 각 요소에서 사용할 수 있음. 객체의 경우는 key
* v-for 사용시 <u>반드시 key 속성을 각 요소에 작성</u>
* v-if와 함께 사용하는 경우 v-for가 우선순위가 더 높음

v-on

* 엘리먼트에 이벤트 리스너를 연결
* 이벤트 유현은 전달인자로 표시함
* 특정 이벤트가 발생했을 때, 주어진 코드가 실행됨
* 약어 : @

v-bind

* HTML 요소의 속성에 Vue의 상태 데이터를 값으로 할당
* Object 형태로 사용하면 value가 true인 key가 class 바인딩 값으로 할당
* 약어 : :(콜론)

v-model

* HTML form 요소의 값과 data를 **양방향 바인딩**
* 한, 중, 일의 경우 원하는 대로 인식이 이루어지지 않으므로 `v-on:input=""` 등으로 사용 
* 수식어
  * .lazy : input 대신 change 이벤트 이후에 동기화
  * .number : 문자를 숫자열로 변경
  * .trim : 입력에 대한 trim을 진행 

---

### Lifecycle Hook

* 각 Vue instance는 생성될 때 일련의 초기화 단계를 가짐

![Vue.js Lifecycle Hooks. In this tutorial you will learn and… | by Sunil  Joshi | JavaScript in Plain English](https://miro.medium.com/max/650/0*auByFHd6tZlHMUGZ.jpg)

---

### lodash library

##### lodash

* 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
* 함수 예시
  * reverse, sortBy, range, random...

