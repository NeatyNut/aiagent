from tools import init_plan, add_plan, delete_plan, get_plan_dict
from system_prompt import *
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from state import Agent_State
from state_method import update_agent_state
import json

class Planner_Agent:
    def __init__(self):
        load_dotenv()
        self.name = "planner"
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

    def generate(self, state:Agent_State):
        system_prompt = make_system_prompts(self.name, role_prompts.get(self.name), system_prompts.get(self.name))
        history = json.dumps(state.get("history"))
        response = self.llm.invoke(system_prompt, history, tool_config=[init_plan, add_plan, delete_plan])
        
        update_agent_state(state, self.name, response)
        state["plan"] = get_plan_dict(state["plan"])

        print(f"😒 state : {state}")
        return state

