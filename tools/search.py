from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@tool
def extract_university_url(school_name: str) -> str:
    """Naver를 통해 학교명 검색"""
# Construct the search URL with the school name
    search_url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={school_name}"
    
    try:
        # Send a GET request to the search URL
        response = requests.get(search_url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Raise an exception for bad responses
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Use the provided CSS selector to find the element
        selector = "#main_pack > div.sc_new.cs_common_module.case_normal.color_5._university > div.cm_content_wrap > div:nth-child(1) > div > div.button_area > div > ul > li:nth-child(1) > a"
        element = soup.select_one(selector)
        
        # Extract the href attribute if the element exists
        if element and element.has_attr('href'):
            return element['href']
        else:
            return f"No URL found for school: {school_name}. Element not found with the specified selector."
    
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
@tool
def search_university_info_from_adiga(school_name: str) -> str:
    """대학명으로 adiga.kr 사이트 검색을 수행하는 툴"""
    
    # Chrome 옵션 설정 (헤드리스 모드)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.adiga.kr/man/inf/mainView.do?menuId=PCMANINF1000")
        
        # 검색창 요소 찾기 (실제 사이트 구조에 맞게 수정 필요)
        search_input = driver.find_element(By.NAME, "searchKeyword")
        search_input.send_keys(school_name)
        
        # 검색 버튼 클릭
        search_btn = driver.find_element(By.CSS_SELECTOR, "button.search-btn")
        search_btn.click()
        
        # 결과 대기 및 처리
        driver.implicitly_wait(3)
        result = driver.page_source  # 실제 데이터 추출 로직 추가
        
        return f"{school_name} 검색 완료. 결과 페이지 HTML 길이: {len(result)}"
        
    except Exception as e:
        return f"오류 발생: {str(e)}"
    finally:
        driver.quit()