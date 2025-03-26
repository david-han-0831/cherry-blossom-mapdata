import json
import time
from data.locations import (
    paldang_locations, 
    gwangju_center_locations,
    general_locations,
    drive_courses_meta
)
from utils.naver_api import get_lat_lng, get_route_path

def create_course_points(locations):
    """드라이브 코스의 포인트들을 생성합니다."""
    points = []
    
    # 위도/경도 구하기
    for location in locations:
        lat, lng = get_lat_lng(location["address"])
        if lat and lng:
            location["latitude"] = lat
            location["longitude"] = lng
            print(f"✅ {location['name']}: 위도 {lat}, 경도 {lng}")
        else:
            print(f"❌ {location['name']}: 좌표를 찾을 수 없습니다")
    
    # 경로 포인트 생성
    for i in range(len(locations)):
        current_location = locations[i]
        points.append({
            "name": current_location["name"],
            "address": current_location["address"],
            "latitude": current_location["latitude"],
            "longitude": current_location["longitude"],
            "description": current_location["description"],
            "isMainPoint": True
        })
        
        if i < len(locations) - 1:
            next_location = locations[i + 1]
            path = get_route_path(
                current_location["longitude"],
                current_location["latitude"],
                next_location["longitude"],
                next_location["latitude"]
            )
            
            for point in path[1:-1]:
                points.append({
                    "latitude": point[1],
                    "longitude": point[0],
                    "isMainPoint": False
                })
            
            time.sleep(1)
    
    return points

def generate_location_data():
    """최종 위치 데이터를 생성합니다."""
    drive_courses = []
    
    # 각 드라이브 코스에 대해 포인트 생성
    for course_meta in drive_courses_meta:
        points = create_course_points(course_meta["locations"])
        drive_courses.append({
            "id": course_meta["id"],
            "name": course_meta["name"],
            "description": course_meta["description"],
            "distance": course_meta["distance"],
            "duration": course_meta["duration"],
            "points": points
        })
    
    # 최종 데이터 구조 생성
    location_data = {
        "locations": general_locations,
        "driveCourses": drive_courses
    }
    
    return location_data

def main():
    """메인 실행 함수"""
    location_data = generate_location_data()
    
    # JSON 형식으로 저장
    with open("location_data.json", "w", encoding="utf-8") as f:
        json.dump(location_data, f, ensure_ascii=False, indent=2)
    
    print("\n📝 location_data.json 파일이 생성되었습니다.")

if __name__ == "__main__":
    main()
