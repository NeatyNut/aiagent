import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-flash")
response = model.generate_content("대한민국 고3 입시 전략을 설명해줘")
print(response.text)

#---

from agents.planner import plan_from_query
from agents.university_choicer import choose_universities
from agents.apply_file_getter import get_admission_guides
# from agents.possible_checker import check_eligibility
# from agents.calculator import calculate_score

if __name__ == "__main__":
    user_query = "내 성적에 맞는 수시 대학 추천해줘"

    print("[1] 질의 분석 중...")
    todos = plan_from_query(user_query)
    print("해야 할 일:", todos)

    print("\n[2] 성적 기반 대학 추천 중...")
    sample_grade = {"국어": 2, "수학": 1, "영어": 2, "탐구": 1}
    universities = choose_universities(sample_grade)
    print("추천 대학:", universities)

    print("\n[3] 입학 요강 찾는 중...")
    guides = get_admission_guides(universities)
    for univ, link in guides.items():
        print(f"{univ}: {link}")