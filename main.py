from langchain.agents import initialize_agent
from langchain.agents import AgentType
from tools.search import extract_university_url, search_university_info_from_adiga
from langchain.memory import ConversationBufferMemory
from LLM.instance_ai import get_aiagent

# 사용할 툴 리스트
tools = [extract_university_url, search_university_info_from_adiga]

# Agent 초기화
agent = initialize_agent(
    tools=tools,
    llm=get_aiagent().llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory = ConversationBufferMemory(memory_key="chat_history")
)

agent.invoke("수원대 url을 줄래?")