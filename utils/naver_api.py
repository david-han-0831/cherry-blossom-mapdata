import requests
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경 변수에서 API 키 가져오기
NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

def get_lat_lng(address):
    """주소로부터 위도/경도를 가져옵니다."""
    url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": NAVER_CLIENT_ID,
        "X-NCP-APIGW-API-KEY": NAVER_CLIENT_SECRET
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()

    if "addresses" in data and len(data["addresses"]) > 0:
        lat = data["addresses"][0]["y"]
        lng = data["addresses"][0]["x"]
        return float(lat), float(lng)
    else:
        return None, None

def get_route_path(start_lng, start_lat, goal_lng, goal_lat):
    """두 지점 사이의 자동차 경로를 가져옵니다."""
    url = f"https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start={start_lng},{start_lat}&goal={goal_lng},{goal_lat}&option=trafast"
    
    headers = {
        "X-NCP-APIGW-API-KEY-ID": NAVER_CLIENT_ID,
        "X-NCP-APIGW-API-KEY": NAVER_CLIENT_SECRET
    }
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    return data["route"]["trafast"][0]["path"] if 'route' in data else [] 