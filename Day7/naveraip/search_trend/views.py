from django.shortcuts import render
import json
import requests
# Create your views here.

def search(request):
    # 검색어 입력하는 곳

    return render(request, 'search.html')

def result(request):
    start_date = request.GET['search_start_date']
    end_date = request.GET['search_end_date']
    time_unit = request.GET['search_time_unit']
    group_name = request.GET['search_group_name']
    keywords = request.GET['search_keywords'].split(',')

    query = {
        "startDate": start_date,
        "endDate": end_date,
        "timeUnit": time_unit,
        "keywordGroups": [
            {
                "groupName": group_name,
                "keywords": keywords
            }
        ]
    }
    url = 'https://openapi.naver.com/v1/datalab/search'
    client_id ='F7ObMOlFh01Wvu5lJy_N'
    client_secret = '_uFPcV_pwE'
    
    headers = {
        'X-Naver-Client-Id' : client_id,
        'X-Naver-Client-Secret' : client_secret
    }
    #query를 json으로 
    params = json.dumps(query)

    response = requests.post(url, data=params, headers=headers)
    result = response.text
    context = {
        'result' : result
             
    }
    return render(request, 'result.html', context, result)