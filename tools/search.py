from langchain.tools import tool
from playwright.sync_api import sync_playwright
from datetime import datetime

@tool
def GET_Uni_code(uni:str):
    """
    어디가 사이트 내 대학코드 얻기(uni_code)

    Args:
        uni (str) : 검색할 대학명
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page("https://www.adiga.kr/ucp/uvt/uni/univView.do?menuId=PCUVTINF2000")
        page.locator("#searchTitle").fill(uni)
        page.locator("#frm > div > div.ltCont > div > div.cptSearchIpt > div > a").click()
        uni_code = page.locator("#tbResult > table > tbody > tr > td:nth-child(1) > span > a").get_attribute("code")
        browser.close()
    return uni_code

@tool
def GET_Uni_Base_Info(uni:str):
    """
    대학 주소/전화, 수시 모집요강, 정시 모집요강, 입학처 홈페이지 등을 얻을 수 있는 어디가 사이트 주소를 제공합니다.

    Args:
        uni (str) : 검색할 대학명
    """
    print(f"되고 있는거야? : {uni}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page("https://www.adiga.kr/ucp/uvt/uni/univView.do?menuId=PCUVTINF2000")
        page.locator("#searchTitle").fill(uni)
        page.locator("#frm > div > div.ltCont > div > div.cptSearchIpt > div > a").click()
        page.locator("#tbResult > table > tbody > tr > td:nth-child(1) > span > a").click()
        browser.close()
    return page.url

# @tool
# def GET_Addmission_Score(uni_code: str, year:int, kind:Literal["학생부종합전형", "학생부교과전형", "수능위주전형"]) -> str:
#     """
#     대학의 전형유형 입시 결과 페이지 URL을 반환합니다.
    
#     Args:
#         uni_code (str): 검색할 대학 코드(Get_uni_code tool을 통해 획득 가능)
#         year (int): 조회할 연도(작년 입학성적 조회를 위해선 올해 연도보다 1년 추가한 값 기입 ex if today == 2025 => 2026)
#         kind (str): 전형유형

#     Returns:
#         str: 입시 결과 페이지 URL
#     """

#     indexs = {
#         "학생부종합전형" : 20,
#         "학생부교과전형" : 30,
#         "수능위주전형" : 40
#     }


#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto(f"https://www.adiga.kr/uct/acd/ade/criteriaAndResultPopup.do?unvCd={uni_code}&searchSyr={year}&tsrdCmphSlcnArtclUpCd={indexs[kind]}")
#         page.locator(f"button.accordionBtn:has-text('2. {year-1}학년도 전형 결과')").click()
#         page.wait_for_selector(".popupCmpList", state="visible", timeout=10000)
#         ## 열어서 내부 데이터를 가져오는 법 찾는 중 ::: Ctrl+U에서 	//컨텐츠 검색 함수에서 막힘
        
#         return page.url