# Vue Router

### Vue Router

* "Vue.js 공식 라우터"
* route에 component를 mapping한 후, 어떤 주소에서 rendering 할 지 알려줌
* SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공

##### Vue Router 시작하기

```bash
// 프로젝트 생성 및 이동
$ vue create my-router-app
$ cd my-router-app

// node modules를 통해서 git을 통해 받은 file은 환경을 맞춰줌
$ npm i

// Vue Router plugin 설치
$ vue add router
```

##### Vue Router로 인한 변화

1. App.vue 코드
2. router/index.js 생성
3. views Directory 생성

```javascript
// router/index.js

import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)
const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        component: Avout
    }
]
```

```vue
<template>
	<div id="app">
        <router-link to='/'>Home</router-link>
        <router-link to='/about'>About</router-link>
    </div>
</template>
```

##### router-link

* 사용자 네비게이션을 가능하게 하는 컴포넌트
* 목표 경로는 'to' prop으로 지정됨
* HTML5 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 브라우저가 페이지를 다시 로드 하지 않도록 함
* a 태그지만, 우리가 알고있는 GET 요청을 보내는 a 태그와는 다르게 기본 GET 요청을 보내는 이벤트를 제거한 형태

##### router-view

* 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
* 실제 component가 DOM에 부착되어 보이는 자리를 의미
* router-link를 클릭하면 해당 경로와 연결되어 있는 index.js에 정의한 컴포넌트가 위치

### History mode

* HTML History API를 사용해서 router를 구현한 것
* 브라우저의 히스토리는 남기지만 실제 페이지는 이동하지 않는 기능을 지원
* 페이지를 다시 로드하지 않고 URL을 변경할 수 있음 => 새로고침이 되지 않는다 => SPA의 단점을 해결



### Vue Routes

##### 1. Named Routes

```vue
<template>
	<div id="app">
        <router-link :to='{name : 'Home'}'>Home</router-link>
        <router-link :to='{name : 'About'}'>About</router-link>
        <router-link :to='{name : 'TheLotto', params : { lottoNum: 6}}'>The Lotto</router-link>
    </div>
</template>
```

##### 2. 프로그래밍 방식 네비게이션

```vue
// About.vue
<template>
	<div class="about">
        <button @click="moveToHome">
        	Home으로 이동!    
    	</button>
    </div>
</template>
<script>
export default {
    name: 'About',
    methods: {
        moveToHome: function(){
            //this.$router.push('/')
        	this.$router.push({ name: 'Home '})
        }
    }
}
</script>
```

##### 3. Dynamic Route Matching

* 동적 인자 전달 (`:` 콜론으로 시작)
* 주어진 패턴을 가진 라우트를 동일한 컴포넌트에 매핑해야하는 경우
* 예) 모든 User에 대하여 동일한 레이아웃을 가지지만, 다른 User ID로 렌더링 되어야하는 User Component (profile page)
* 컴포넌트에서 this.$route.params

```javascript
// index.js

Vue.use(VueRouter)

const routes = [
	{
		path: '/lotto/:lottoNum',
		name: 'Lotto',
		component: Lotto
	},
]
```

```vue
// src/views/TheLotto.vue

<template>
	<div>
        <p>{{ $route.params }}</p>
        <p>{{ $route.params.lottoNum }}개의 번호를 추첨합니다.</p>
        <button @click="getLuckyNum">Pick!</button>
        <p>{{ selectedLuckyNum }}</p>
    </div>
</template>

<script>
	import _ from 'lodash'
    export default {
        name: 'TheLotto',
        data: function() {
            return {
                selectedLuckyNum: []
            }
        },
        methods: {
            getLuckyNum: function() {
                const numbers = _.range(1, 46)
                this.selectedLuckyNum = _.sampleSize(numbers, this.$route.params.lottoNum)
            }
        }
    } 
</script>
```



### components와 views

* 정해진 구조가 있는 것은 아니지만, 보통 다음과 같이 구조화해서 활용
* App.vue
  * 최상위 component
* views/
  * router(index.js)에 mapping되는 component들을 모아두는 folder
* components/
  * router에 mapping된 component 내부에 작성하는 component들을 모아두는 folder



### Vue Router가 필요한 이유

##### 1. SPA 등장 이전

* 서버가 모든 라우딩을 통제
* 요청 경로에 맞는 HTML을 제공

##### 2. SPA 등장 이후

* 서버는 index.html 하나만 제공
* 이후 모든 처리는 HTML 위의 JS 코드를 활용해 진행
* 요청에 대한 처리를 더이상 서버가 하지 않음

##### 3. 라우팅 처리 차이

