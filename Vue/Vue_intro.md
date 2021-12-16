# Vue

### Vue.js Intro

##### SPA

* Single Page Appliacation
* 단일 페이지로 구성되며 서버로부터 최초에만 페이지를 다운로드하고, 이후에는 동적으로 DOM을 구성
* 연속되는 페이지 간의 사용자 경험(UX)을 향상
  * 모바일 사용량이 증가하고 있는 현재, 트래픽의 감소와 속도, 사용성, 반응성의 향상은 매우 중요하기 때문
* 동작 원리의 일부가 CSR(Client Side Rendering)의 구조를 따름

##### CSR

* Client Side REndering
* 서버에서 화면을 구성하는 SSR 방식과 달리 클라이언트에서 화면을 구성
* 최초 요청 시 HTML, CSS, JS 등 데이터를 제외한 각종 리소스를 응답받고 이후 클라이언트에서는 필요한 데이터만 요청해 JS로 DOM을 렌더링하는 방식
* SPA가 사용하는 렌더링 방식
* 장점
  * 서버와 글라이언트 간 트래픽 감소
  * 사용자 경험(UX) 향상
* 단점
  * SSR에 비해 전체 페이지 렌더링 시점이 느림
  * SEO(검색 엔진 최적화)에 어려움이 있음(최초 문서에 데이터가 없기 때문)

##### SSR

* Server Side Rendering
* 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식
* 장점
  * 초기 구동 속도가 빠름 : 클라이언트가 빠르게 컨텐츠를 볼 수 있음
  * SEO(검색 엔진 최적화)에 적합 : DOM에 이미 모든 데이터가 작성되어있기 때문
* 단점
  * 모든 요청마다 새로운 페이지를 구성하여 전달
  * 반복되는 전체 새로고침으로 인해 사용자 경험이 떨어짐
  * 상대적으로 트래픽이 많아 서버의 부담이 클 수 있음





### Concepts of Vue.js

##### MVVM Pattern

* 구성요소
  1. Model
     * JavaScript Object
     * 이 Object는 Vue Instance 내부에서 data로 사용되는데, 이 값이 바뀌면 View(DOM)가 반응
  2. View
     * DOM(HTML)
     * Data의 변화에 따라서 바뀌는 대상
  3. View Model
     * 모든 Vue Instance
     * View와  Model 사이에서 Data와 DOM에 관련된 모든 일들을 처리
     * ViewModel을 활용하여 Data를 얼마만큼 잘 처리해서 보여줄 것인지(DOM)를 고려



##### Django & Vue.js

Django

* "데이터의 흐름"
* url -> views -> template

Vue.js

* Data가 변화하면 DOM이 변경
  1. Data 로직 작성
  2. DOM 작성