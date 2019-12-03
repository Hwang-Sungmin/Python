# Day10

##### RESTful api

| 역할   | Request-Method | End-point              | Views(Function) | 기존역할   |
| ------ | -------------- | ---------------------- | --------------- | ---------- |
| Create | GET            | /articles/new/         | new             | 새글 form  |
| Create | POST           | /articles/             | create -> new   | 새글       |
| Read   | GET            | /articles/<id>/        | show            | 글 하나    |
| Read   | GET            | /articles/             | index           | 전체리스트 |
| Update | GET            | /articles/<id>/edit/   | edit            | 수정 form  |
| Update | POST           | /articles/<id>/edit/   | update -> edit  | 수정반영   |
| Delete | POST           | /articles/<id>/delete/ | delete          | 삭제       |

- Request-Method에 따라 다른 Logic 구현

  - POST방식으로 값을 넘길때는 crsf 보안을 해서 제한을 한다.
  - csrf 토큰을 통해 해당 웹에서 발생한 post임을 확인.
  - Cross-site 문제를 막기위한 간단한 방법.

  ````python
  <input type="text" name="csrfmiddelewaretoken" value="{{csrf_token}}">
  ````