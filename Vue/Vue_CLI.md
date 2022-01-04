# Vue CLI

### SFC

##### Component

* 기본 HTML 엘리먼트를 확장하여 재사용 가능한 코드를 캡슐화 하는데 도움을 줌
* CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
* 즉, 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라, 재사용성의 측면에서도 매우 강력한 기능을 제공

##### SFC(Single File Component)

* Vue의 컴포넌트 기반 개발의 핵심 특징

* 하나의 컴포넌트는 .vue 확장자를 가진 하나의 파일 안에서 작성되는 코드의 결과물

* 화면의 특정 영역에 대한 HTML, CSS, JavaScript 코드를 하나의 파일(.vue)에서 관리

* 즉, .vue 확장자를 가진 싱글 파일 컴포넌트를 통해 개발하는 방식

  ​	Vue Component === Vue Instance === .vue File

---

### Vue CLI

##### Vue CLI

* Vue,js 개발을 위한 표준 도구
* 프로젝트 구성을 도와주는 역할을 하며 Vue 개발 생태계에서 표준 tool 기준을 목표로 함

##### Node.js

* 자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경

##### NPM(Node Package Manage)

* 자바스크립트 언어를 위한 패키지 관리자
  * Python - pip, Node.js - NPM



##### Vue CLI Quick Start

```bash
# 설치
$ npm install -g @vue/cli

# 버전 확인
$ vue --version
```

```bash
# git-bash가 아닌 vscode terminal로 진행

# 프로젝트 생성
$ vue create my-first

# 실행
$ npm run serve
```



---

### Vue Project 구조

##### Babel 

* "JavaScript compiler"
* 자바스크립트의 코드를 이전 버전으로 번역/변환 해주는 도구
* 최신 버전을 구 버전으로 옮기는 번역기가 등장하면서 개발자들은 더 이상 내 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있게 됨

##### Webpack

* "Static Module bundler"
* 모듈 간의 의존성 문제를 해결하기 위한 도구
* 프로젝트에 필요한 모든 모듈을 mapping, 내부적으로 종속성 그래프를 빌드
* Module의 의존성 문제를 해결해주는 작업을 Bundling
* 여러 모듈을 하나로 묶어주고 묶인 파일은 하나(혹은 여러개)로 합쳐짐

##### 프로젝트 구조

* node_modules
  * node.js 환경의 여러 의존성 모듈

---

* public/index.html
  * Vue 앱의 뼈대가 되는 파일
  * 실제 제공되는 단일 html

---

* src/assets
  * webpack에 의해 빌드된 정적 파일
* src/components
  * 하위 컴포넌트들이 위치
* src/App.vue
  * 최상위 컴포넌트
* src/main.js
  * webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
  * 실제 단일 파일에서 DOM과 data를 연결했던 것과 동일한 작업이 이루어지는 곳
  * Vue 전역에서 활용할 모듈을 등록할 수 있는 파일

---

* babel.config.js
  * babel 관련 설정이 작성된 파일
* package.json
  * 프로젝트의 종속성 목록과 지원되는 브러우저에 대한 구성 옵션이 포함
* package-lock.json
  * node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
  * 사용할 패키지의 버전을 고정
  * 개발 과정 간의 의존성 패키지 충돌 방지



# Pass Props & Emit Events

### component

##### component 작성

* Vue app은 자연스럽게 중첩된 컴포넌트 트리로 구성됨
* 컴포넌트 간 부모-자식 관계가 구성되며 이들 사이에 필연적으로 의사 소통이 필요함
* 부모는 자식에게 <u>데이터를 전달</u>(Pass **props**)하며, 자식은 부모에게 <u>메세지를 보내므로</u> 알림(Emit **event**)

##### component 구조

1. 템플릿(HTML)
   * HTML의 body
   * 각 컴포넌트를 작성
2. 스크립트(JavaScript)
   * 컴포넌트의 정보, 데이터, 메서드 등 vue instance를 구성하는 대부분이 작성
3. 스타일(CSS)
   * component의 style을 담당

##### component 등록

1. 불러오기
2. 등록하기
3. 보여주기

---

### props

##### props

* 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
* 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함
* 즉, 데이터는 props 옵션을 사용하여 자식 컴포넌트로 전달됨

### Static Props 작성

```vue
// App.vue

<template>
	<div id="app">
        <about my-message="This is prop data"></about>
    </div>
</template>

<script>
import About from './components/About.vue'
export default {
    name: 'App',
    components: {
        About,
    }
}
</script>
```

```vue
// About.vue

<template>
	<div id="app">
        <p>{{ myMessage }}</p>
    </div>
</template>

<script>
export default {
    name: 'About',
    props: {
        myMessage: String,
    }
}
</script>
```

* 자식 컴포넌트(About.vue)에 보낼 prop 선언
* prop-data-name="value"

##### Dynamic Props 작성

```vue
// App.vue

<template>
	<div id="app">
        <about
            :parent-data="parentData"
        >
    	</about>
    </div>
</template>

<script>
import About from './components/About.vue'
export default {
    name: 'App',
    components: {
        About,
    },
    data: function () {
        return {
            parentData: 'This is parent data by v-bind',
        }
    }
}
</script>
```

```vue
// About.vue

<template>
	<div id="app">
        <p>{{ parentData }}</p>
    </div>
</template>

<script>
export default {
    name: 'About',
    props: {
        parentData: String,
    }
}
</script>
```

##### Props 이름 컨벤션

* declaration(선언 시) : camelCase
* in template(HTML) : kebab-case

---

##### **component의 'data'는 반드시 함수여야 함**

* 기본적으로 각 인스턴스는 모두 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)해야 함
* 그렇지 않으면 각 인스턴스가 모두 같은 data 객체를 공유

##### Props시 자주하는 실수

* Static 구문을 사용하여 숫자를 전달하려고 시도
* 값이 JavaScript 표현식으로 평가되도록 v-bind를 사용해야 함

```Html
<!-- 일반 문자열 "1" 전달-->
<compo some-prop="1"></compo>

<!-- 실제 숫자 "1" 전달-->
<comp :some-prop="1"></comp>
```

---

##### 단방향 데이터 흐름

* 모든 props는 하위 속성과 상위 속성 사이의 단방향 다인딩을 형성
* 부모의 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향으로는 안 됨
* 부모 컴포넌트가 업데이트 될 때마다 자식 요소의 모든 prop들이 최신 값으로 업데이트

---

### Emit Event

##### Emit

* "Listening to Child Components Events"
* $emit(eventName)
* 부모 컴포넌트는 자식 컴포넌트가 사용되는 템플릿에서 v-on을 사용하여 자식 컴포넌트가 보낸 이벤트를 청취

##### Emit event 작성

* 현재 인스턴스에서 $emit 인스턴스 메서드를 사용해 child-input-change 이벤트를 트리거

```vue
// About.vue
<template>
	<div id="app">
        <input
            type="text"
            @keyup.enter="childInputChange"
            v-modle="childInputData"
        >
    </div>
</template>

<script>
export default {
    name: 'About',
    data: function () {
        return {
            childInputData: null,
        }
    },
    methods: {
        childInputChange: funtion() {
        	this.$emit('child-input-change', this.childInputData)
    	}
    }
}
</script>
```

```vue
// App.vue

<template>
    <about
        @child-input-change="parentGetChange"
    >
    </about>
</template>

<script>
import About from '.components/About.vue'
export default {
    name: 'App',
    components: {
        About,
    },
    methods: {
        parentGetChange: function (inputData) {
            console.log('About으로부터 ${inputData}를 받음')
        }
    }
}
</script>
```

##### event 이름 컨벤션

* 컴포넌트 및 props와 달리, 이벤트는 자동 대소문자 변환을 제공하지 않음
* HTML의 대소문자 구분을 위해 DOM 템플릿의 v-on 이벤트 리스너는 항상 자동으로 소문자 변환되기 때문에 `v-on:myEvent`는 자동으로 `v-on:myevent`로 변환
* 이러한 이유로 이벤트 이름에는 **항상 kebab-case를 사용**하는 것을 권장

```vue
this.$emit('myEvent')
```

```vue
<!-- 이벤트가 동작하지 않음-->
<my-component @my-event="doSomething"></my-component>
```

