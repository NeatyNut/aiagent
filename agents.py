from system_prompt import *
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from state import AgentState
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import add_messages
from tools import init_plan, add_plan, delete_plan, get_plan_dict

class PlannerAgent:
    def __init__(self):
        load_dotenv()
        self.name = "planner"
        self.llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0)
        self.llm.bind(tools=[init_plan])

    def generate(self, state:AgentState):
        user_input = input(f'😒시키실 업무 입력 >>> ')
        system_prompt = make_system_prompts(self.name, role_prompts.get(self.name, ""), system_prompts.get(self.name, ""))        
        prompt = [SystemMessage(content=system_prompt), HumanMessage(content=user_input)]
        state["messages"] = prompt
        
        aimessage = self.llm.invoke(state["messages"])
        state["messages"] = add_messages(state["messages"], aimessage)
        return state