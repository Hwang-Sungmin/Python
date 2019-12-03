from flask import Flask, escape, request
import requests

# 기본 구조
app = Flask(__name__)

#debug 모드
# 수정시 서버를 자동으로 재실행 
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def index():
    daily_toon_data = {}
    day = 'mon'    
    url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
    return request_json_data_from_url(url)
    

def request_json_data_from_url(url):
    response = requests.get(url)
    data = response.json()
    return data