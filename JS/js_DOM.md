## JavaScript

### DOM 조작 

#### 개념

1. 선택(Select)
2. 변경(Manipulation)

#### DOM 관련 객체의 상속 구조

* Element
  * Document 안의 모든 객체가 상속하는 가장 범용적인 기반 크래스
  * 부모인 Node와 그 부모인 EventTarget의 속성을 상속
* Document
  * 브라우저가 불러온 웹 페이지를 나타냄
  * DOM 트리의 진입점(entry point) 역할을 수행
* HTML Element
  * 모든 HTML 요소
  * 부모 element의 속성 상속

### DOM 선택

* Document.**querySelector**(selector)
  * 제공한 선택자와 일치하는 element 하나 선택
  * 제공한 CSS Selector을 만족하는 첫 번째 element 객체를 반환(없다면 null)

* Document.**querySelectorAll**(selector)
  * 제공한 선택자와 일치하는 여러 element를 선택
  * 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  * 지정된 셀렉터에 일치하는 <u>NodeList를 반환</u>
    * NodeList?
    * index로만 각 항목에 접근 가능
    * HTML Collection과 달리 배열에서 사용하는 forEach 함수 및 다양한 메서드 사용 가능
    * Static Collection으로 실시간으로 결과가 반영되지는 않음
* getElementById(id)
* getElementByTagName(name)
* getElementsByClassName(names)

```html
document.querySelector('#id')
document.querySelectAll('.name')

# > : 자식 선택자
#   : 자손 선택자
```



---

### DOM 변경

* Element.**append**()
  * 특정 부모 Node의 자식 Nodelist 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
  * 여러 개의 Node 객체, DOMString을 추가할 수 있음
  * 반환 값이 없음
* Node.**appendChild**()
  * 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입(Node만 추가 가능)
  * 한 번에 오직 하나의 Node만 추가할 수 있음
  * 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동

* Node.**innerText**
  * Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현(사람이 읽을 수 있는 요소만 남김)
  * 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
* Element.**innerHTML**
  * 요소(element) 내에 포함된 <u>HTML 마크업을 반환</u>
  * [주의] XSS 공격에 취약하므로 주의

### DOM 삭제

* ChildNode.remove()
  * Node가 속한 트리에서 해당 Node를 제거
* Node.removeChilde()
  * DOM에서 자식 Node를 제거하고 제거된 Node를 반환
  * Node는 인자로 들어가는 자식 Node의 부모 Node

### DOM 속성

* Element.setAttribute(name, value)
  * 지정된 요소의 값을 설정
  * 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
* Element.getAttribute(attributeName)
  * 해당 요소의 지정된 값(문자열)을 반환
  * 인자(attributeName)는 값을 얻고자 하는 속성의 이름

