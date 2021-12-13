# AJAX

### AJAX

##### AJAX란?

* Asynchronous JavaScript And XML(비동기식 JavaScript와 XML)
* 서버와 통신하기 위해 **XMLHttpRequest** 객체를 활용

##### AJAX 특징

* 페이지 전체를 reload(새로고침) 하지 않고서도 수행되는 **"비동기성"**
  1. 페이지를 새로고침 없이 서버에 요청
  2. 서버로부터 데이터를 받고 작업을 수행

##### XMLHttpRequest 객체

* 서버와 상호작용하기 위해 사용되며 전체 페이지의 새로고침 없이 데이터를 받아올 수 있음
* 사용자의 작업을 방해하지 않으면서 페이지 일부를 업데이트 할 수 있음
* 주로 AJAX 프로그래밍에 사용
* 생성자 : **XMLHttpRequest()**

---

### Synchronous & Asynchronous

##### 동기식

* 순차적, 직렬적 Task 수행
* 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐(blocking)

##### 비동기식

* 병렬적 Task 수행
* 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐(non-blocking)

##### JavaScript는 single threaded 이다.

1. 즉시 처리하지 못하는 이벤트들을 **다른 곳(Wev API)**으로 보내서 처리하도록 하고.
2. 처리된 이벤트들을 처리된 순서대로 **대기실(Task queue)**에 줄을 세워 놓고
3. Call Stack이 비면 **담당자(Event Loop)**가 대기 줄에서 가장 오래된(제일 앞의) 이벤트를 Call Stack으로 보냄

##### Concurrency model

* Event loop를 기반으로 하는 **동시성 모델**

1. Call Stack
   * 요청이 들어올 떄마다 해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 구조
2. Web API(Browser API)
   * JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
   * **setTimeout(), DOM events 그리고 AJAX로 데이터를 가져오는 시간이 소요되는 일들을 처리**
3. Task Queue
   * 비동기 처리된 callback  함수가 대기하는 Queue(FIFO) 형태의 자료 구조
   * main thread가 끝난 후 실행되어 후속 JavaScript 코드가 차단되는 것을 방지
4. Event Loop
   * CallStack이 비어 있는지 확인
   * 비어 있는 경우 Task Queue에서 실행 대기 중인 callback 함수가 있는지 확인
   * Task Queue에 대기 중인 callback 함수가 있다면 가장 앞에 있는 callback 함수를 Call Stack으로 push

```javascript
console.log('Hi~')
setTimeout(function eat() {
    console.log('yummy')
}, 3000)
console.log('Bye~')

> Hi
> Bye
> yummy
```







### Promise

##### Promise object 

* 비동기 작업의 최종 완료 또는 실패를 나타내는 객체
* .then(callback)
  * 이전 작업(promise)이 성공했을 때 수행할 작업을 나타내는 callback 함수
* .catch(callback)
  * .then이 하나라도 실패하면 동작
  * 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용할 수 있음
* **반드시 반환 값이 있어야 함**
* .finally(callback)
  * Promise 객체를 반환
  * 결과와 상관없이 무조건 지정된 callback 함수가 실행
  * 어떠한 인자도 전달받지 않음 : Promise가 성공되었는지 거절되었는지 판단할 수 없기 떄문
  * 무조건 실행되어야 하는 절에서 활용



