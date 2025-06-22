from langchain.agents import initialize_agent
from langchain.agents import AgentType
from tools.search import GET_Uni_code, GET_Uni_Base_Info
from langchain.memory import ConversationBufferMemory
from LLM.instance_ai import get_aiagent

# 사용할 툴 리스트
tools = [GET_Uni_code, GET_Uni_Base_Info]

# Agent 초기화
agent = initialize_agent(
    tools=tools,
    llm=get_aiagent().llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory = ConversationBufferMemory(memory_key="chat_history")
)

agent.invoke("서울대 올해 의예과 모집인원을 알 수 있을까?")