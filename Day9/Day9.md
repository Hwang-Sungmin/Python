# Day9

- 오늘한 것
- 기본 setting
  - pip install pylint
  - pip install pylint-django
  - 환경변수에서 Paht 설정 중 python 관련 부분 뗴어와 vscode 창에 붙여넣기
    -  ctrl'p' 파레트에서 >setting 후 경로 붙여넣기



#####  URL namespace

- 각각의 url에 별명을 지어줘서 html파일에서 사용하는 링크를 추가적으로 바꾸지 않고, urls.py에서만 수정하면 html 파일에서도 링크 수정이 반영되게끔 한다.
  - GET -> 조회(select), POST -> DB에 반영

| 역할   | Request-Method | End-point              | Views(Function) |
| ------ | -------------- | ---------------------- | --------------- |
| Create | GET            | /articles/new/         | new             |
| Create | POST           | /articles/             | create          |
| Read   | GET            | /articles/<id>/        | show            |
| Read   | GET            | /articles/             | index           |
| Update | GET            | /articles/<id>/edit/   | edit            |
| Update | POST           | /articles/<id>/        | update          |
| Delete | POST           | /articles/<id>/delete/ | delete          |



#####  Instance Method

- 



#####  admin

