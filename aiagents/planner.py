# 구조 짜기

from typing import List

def plan_from_query(query: str) -> List[str]:
    """
    사용자의 질문을 받아 필요한 작업 리스트(todo)를 만들어냄
    """
    # 실제론 LLM 사용, 지금은 예시로 단순 분기
    if "지원 가능한 대학" in query:
        return [
            "성적대 파악",
            "대학 추천",
            "요강 찾기",
            "지원 자격 확인",
            "산식 계산"
        ]
    else:
        return ["질문 분석 실패"]