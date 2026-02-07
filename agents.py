from system_prompt import *
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from state import AgentState
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import add_messages
from tools import init_plan
import os

class PlannerAgent:
    def __init__(self):
        load_dotenv()
        self.name = "planner"
        self.description = "사용자 목표를 분석해 논리적 순서로 구성된 단계별 작업을 설계합니다."
        self.instructions = INSTRUCTIONS[self.name]
        self.llm = ChatGoogleGenerativeAI(model=os.getenv("MODEL", "gemini-3-flash-preview"), temperature=0)
        # self.llm.bind_tools([init_plan])

    def generate(self, state: AgentState):
        # 1. 사용자 입력 받기 (테스트용)
        user_input = input(f'😒시키실 업무 입력 >>> ')
        
        # 2. 시스템 프롬프트 구성 및 메시지 설정
        # system_prompt = make_system_prompt(self.name, self.description, self.instructions)
        messages = [HumanMessage(content=user_input)]
        
        # 3. LLM 호출 (bind_tools 사용 권장)
        # self.llm = ChatGoogleGenerativeAI(...).bind_tools([init_plan])
        aimessage = self.llm.invoke(messages)
        print(aimessage)
        
        # 4. Tool Call이 있는지 확인하고 실행하기
        updates = {"messages": [aimessage]} # 메시지 기록 업데이트 준비
        
        if aimessage.tool_calls:
            for tool_call in aimessage.tool_calls:
                if tool_call["name"] == "init_plan":
                    # 툴 실행 (args에는 LLM이 추출한 'tasks' 리스트가 들어있음)
                    # init_plan은 dict[int, tuple]를 반환함
                    tasks_result = init_plan.invoke(tool_call["args"])
                    updates["tasks"] = tasks_result  # 👈 핵심: state["tasks"]에 담기도록 반환
                    
        return updates # 수정된 부분만 반환하면 LangGraph가 알아서 merge합니다.