# 환경 설정하기

```sh
# 프로젝트 폴더 다운받을 위치로 이동
$ cd '적당한 위치'

$ python -V # 3.7.X 확인

# clone repo
$ git clone  https://github.com/eduyu/4th5iot_b_django_advance.git

# 다운로드한 프로젝트 폴더로 진입
$ cd 4th5iot_b_django_advance

# git 폴더 삭제
$ rm -rf .git

# 가상(독립)환경 생성
$ python -m venv venv

# Windows 에서 가상(독립)환경 활성화
$ source venv/Scripts/activate
# Mac os 에서 가상(독립)환경 활성화
$ source venv/bin/activate

# 필요한 pip 패키지 설치
$ pip install -r requirements.txt

# 서버 구동 확인
$ python manage.py runserver 
```

