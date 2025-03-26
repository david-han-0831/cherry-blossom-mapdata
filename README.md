# 🌸 광주시 벚꽃 위치 데이터 수집기

네이버 지도 API를 활용하여 광주시 벚꽃 명소와 드라이브 코스의 위치 데이터를 수집하는 Python 스크립트입니다.

## 🛠 기능

- 주소를 위도/경도 좌표로 변환
- 드라이브 코스 경로 포인트 수집
- JSON 형식으로 데이터 저장

## 📋 필수 요구사항

- Python 3.8 이상
- requests 라이브러리
- Naver Maps API 키

## ⚙️ 환경 설정

1. 필요한 라이브러리 설치
```bash
pip install requests
```

2. 환경 변수 설정
```python
NAVER_CLIENT_ID = "your_client_id"
NAVER_CLIENT_SECRET = "your_client_secret"
```

## 🔍 주요 기능

### 1. 위도/경도 변환
```python
get_lat_lng(address: str) -> tuple
```
- 입력: 주소 문자열
- 출력: (위도, 경도) 튜플

### 2. 드라이브 코스 경로 생성
```python
get_route_path(start_lng: float, start_lat: float, goal_lng: float, goal_lat: float) -> list
```
- 입력: 출발지와 목적지의 위도/경도
- 출력: 경로 포인트 리스트

### 3. JSON 데이터 생성
```python
create_location_data() -> dict
```
- 출력: 위치 정보가 포함된 딕셔너리

## 📤 출력 데이터 형식

```json
{
  "id": 1,
  "name": "위치명",
  "address": "주소",
  "lat": 위도,
  "lng": 경도,
  "description": "설명",
  "isDriveCourse": true/false,
  "courseDetails": {
    "distance": "거리",
    "duration": "소요시간",
    "routePoints": [
      {
        "lat": 위도,
        "lng": 경도,
        "name": "포인트명(옵션)"
      }
      ...
    ]
  }
}
```

## ⚠️ 주의사항

- API 호출 제한을 고려하여 적절한 딜레이 설정 필요
- 대량의 데이터 수집 시 에러 처리 로직 구현 권장
