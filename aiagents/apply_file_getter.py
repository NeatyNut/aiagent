# 구조 짜기

def get_admission_guides(univ_list: list) -> dict:
    """
    각 대학의 입학 요강 링크/문서 위치를 찾음
    """
    guides = {}
    for univ in univ_list:
        guides[univ] = f"https://{univ}.ac.kr/admission/2025_guide.pdf"
    return guides