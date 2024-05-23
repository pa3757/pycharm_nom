import pandas as pd
import json

# CSV 파일 읽기
file_path = 'modified_course_data2.csv'  # 파일 경로를 지정하세요
df = pd.read_csv(file_path)

# "Course_desc" 열을 JSON 배열로 변환하는 함수 정의
def parse_course_desc(desc):
    entries = desc.split('\n')
    parsed_entries = []
    for entry in entries:
        if 'Course_outline :' in entry:
            course_poi, course_outline = entry.split('Course_outline :', 1)
            parsed_entries.append({
                "course_poi": course_poi.strip(),
                "course_outline": course_outline.strip()
            })
    return parsed_entries

# 각 행의 "Course_desc" 열을 파싱하여 JSON 배열로 변환
df['Course_desc'] = df['Course_desc'].apply(parse_course_desc)

# 데이터프레임을 JSON 형식으로 변환
json_data = df.to_json(orient='records', force_ascii=False, indent=4)

# JSON 데이터 저장
json_file_path = 'course_data2.json'  # 저장할 JSON 파일 경로를 지정하세요
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print(f"JSON 데이터가 {json_file_path}에 저장되었습니다.")
