from system_prompt import *
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from state import AgentState
from langchain_core.messages import SystemMessage
from langgraph.graph import add_messages
from tools import init_plan, add_plan, delete_plan, get_plan_dict

class PlannerAgent:
    def __init__(self):
        load_dotenv()
        self.name = "planner"
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
        self.llm.bind(tools=[init_plan, add_plan, delete_plan, get_plan_dict])

    def generate(self, state:AgentState):
        system_prompt = make_system_prompts(self.name, role_prompts.get(self.name, ""), system_prompts.get(self.name, ""))        
        prompt = [SystemMessage(content=system_prompt)]
        for message in state["messages"]:
            prompt.append(message)
        
        aimessage = self.llm.invoke(prompt)
        state["messages"] = add_messages(state["messages"], aimessage)
        return state