from langchain_core.tools import tool

@tool
def search_school(school_name: str) -> str:
    """Naver를 통해 학교명 검색"""
    return f"🔍 '{school_name}'의 경로는 https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={school_name}"