import requests
import json
import random
import time

'''
student_phone_number = {
    "김민지": "010-1234-1234"
}
print(student_phone_number["김민지"])
print(student_phone_number.get("김민지"))
'''

lunch_menu = {
    "20층 식당": {
        "A코스": "돈까스",
        "B코스": "순대국"
    },
    "양자강": {
        "점심메뉴": "탕짬면",
        "특선메뉴": "군만두"
    },
    "대동집": {
        "밥안주": "비빔면",
        "술안주": "오돌뼈"
    }
}
# print(lunch_menu["20층 식당"]["B코스"])
# print(lunch_menu.get("20층 식당").get("B코스"))
lunch_menu["경성불백"] = {
    "한식메뉴": "석쇠불고기",
    "특식메뉴": "돈까스"
}
'''
print(lunch_menu)
lunch_menu["양자강"] = "짜장면"
print(lunch_menu)
print(lunch_menu.keys())
print(lunch_menu.values())
print(lunch_menu.items())
for key, value in lunch_menu.items(): 
    print(key)
    print(value)
print(random.choice(list(lunch_menu.keys())))
print(random.sample(list(lunch_menu.keys()), 2))
'''

def request_json_data_from_url(url):
    # 3. 해당 url에 요청을 보낸다.
    response = requests.get(url)
    data = response.json()
    return data

def parse_daum_webtoon_data(data):
    toons = []
    for toon in data["data"]:
        # 제목의 key는 'title'
        title = toon["title"]

        # 설명의 key는 'introduction'
        desc = toon["introduction"]

        # 장르의 위치는 'cartoon' 안에 'genre'라는 리스트 안에 'name'이라는 key
        genres = []
        for genre in toon["cartoon"]["genres"]:
            genres.append(genre["name"])
        
        # 작가 이름의 위치는 'cartoon'안에 'artists'라는 리스트 안에 'name'이라는 key
        artists = []
        for artist in toon["cartoon"]["artists"]:
            artists.append(artist["name"])
        # 썸네일 이미지의 위치는 'pcThumbnailImage'안에 'url'이라는 키의 값으로 있음
        img_url = toon["pcThumbnailImage"]["url"]
        tmp = {
            title: {
                "desc": desc,
                "writer": artists,
                "img_url": img_url
            }
        }
        toons.append(tmp)
    return toons



# 월요일 부터 일요일까지 각각을 나타내는 문자열을 정한다.
days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
daily_toon_data = {}

for day in days:
    print(day)
    url = f'http://webtoon.daum.net/data/pc/webtoon/list_serialized/{day}'
    data = request_json_data_from_url(url)
    daily_toon_data[day] = parse_daum_webtoon_data(data)
    print(daily_toon_data[day])
    time.sleep(3)