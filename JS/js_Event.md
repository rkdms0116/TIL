# Event

### Event handler 

##### EventTarget.addEventListener(type, listener[, options])

* 지정된 이벤트가 대상에 전달될 떄마다 호출할 함수를 설정
* 이벤트를 지원하는 모든 객체(Element, Document, Window 등)을 대상으로 지정 가능

* type : 반응할 이벤트 유형(대소문자 구분)
* listener : 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체, EventListener 인터페이스 혹은 JS function 객체(콜백 함수)이여야 함

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button type="button">버튼</button>
</body>
<script>
  const btn = document.querySelector('button')

  btn.addEventListener('click', function (event) {
    alert('버튼이 클릭되었습니다.')
    console.log(event)
    // console.log('버튼이 눌렸다!!')
  })

</script>
</html>
```

```html
<body>
  <!-- 1. onclick -->
  <button onclick="alertMessage()">나를 눌러봐!</button>

  <!-- 2-1. addEventListener -->
  <button id="my-button">나를 눌러봐!!</button>
  <hr>

  <!-- 2-2. addEventListener -->
  <p id="my-paragraph"></p>

  <form action="#">
    <label for="my-text-input">내용을 입력하세요.</label>
    <input id="my-text-input" type="text">
  </form>
  <hr>

  <!-- 2-3. addEventListener -->
  <h2>Change My Color</h2>
  <label for="change-color-input">원하는 색상을 영어로 입력하세요.</label>
  <input id="change-color-input"></input>
  <hr>

  <script>
    // 1
    const alertMessage = function () {
      alert('메롱!!!')
    }

    // 2-1
    const myButton = document.querySelector('#my-button')
    myButton.addEventListener('click', alertMessage)

    // 2-2
    const myTextInput = document.querySelector('#my-text-input')
    myTextInput.addEventListener('input', function (event) {
      console.log(event)
      const myPtag = document.querySelector('#my-paragraph')
      myPtag.innerText = event.target.value
    })

    // 2-3
    const colorInput = document.querySelector('#change-color-input')
    
    const changeColor = function () {
      const h2Tag = document.querySelector('h2')
      h2Tag.style.color = event.target.value
    }

    colorInput.addEventListener('input', changeColor)
  </script>
</body>
```

### Event 취소

##### Event.preventDefault()

* 현재 이벤트의 기본 동작을 중단
* 태그의 기본 동작을 작동하지 않게 막음

* 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소

* 취소할 수 없는 이벤트도 존재
  * 취소 가능 여부는 `event.cancelable`을 사용하여 확인할 수 있음

```html
<body>
  <!-- 1. checkbox -->
  <input type="checkbox" id="my-checkbox">
  <hr>

  <!-- 2. submit -->
  <form action="/articles/" id="my-form">
    <input type="text">
    <input type="submit" value="제출!">
  </form>
  <hr>

  <!-- 3. link -->
  <a href="https://google.com/" target="_blank" id="my-link">GoToGoogle</a>
  <hr>
  
  <script>
    // 1
    const checkBox = document.querySelector('#my-checkbox')
    
    checkBox.addEventListener('click', function (event) {
      event.preventDefault()
      console.log(event)
    })

    // 2
    const formTag = document.querySelector('#my-form')

    formTag.addEventListener('submit', function (event) {
      console.log(event)
      event.preventDefault()
      event.target.reset()
    })

    // 3
    const aTag = document.querySelector('#my-link')

    aTag.addEventListener('click', function (event) {
      console.log(event)
      event.preventDefault()
    })

    // 4 : scroll event는 취소할 수 없음
    document.addEventListener('scroll', function (event) {
      console.log(event)
      event.preventDefault()
    })
  </script>
</body>
```

