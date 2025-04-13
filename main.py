from langchain.agents import initialize_agent
from langchain.agents import AgentType
from tools.search import search_school
from LLM.gen_ai import llm

# 사용할 툴 리스트
tools = [search_school]

# Agent 초기화
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)