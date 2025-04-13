from langchain.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()
results = search.run("서울대학교 수시 모집 요강 2025")
print(results)