from tools import *
from system_prompt import *
from langchain_google_genai import ChatGoogleGenerativeAI
import inspect
from dotenv import load_dotenv
from state import Agent_State

class Planner_Agent:
    def __init__(self):
        load_dotenv()
        self.name = "planner"
        self.planning_tool = planner_tool()
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, tool=[func for name, func in inspect.getmembers(self.planning_tool, predicate=inspect.ismethod)])

    def generate(self, state:Agent_State):
        system_prompt = make_system_prompts(self.name, role_prompts.get(self.name), system_prompts.get(self.name))
        history = json.dumps(state.get("history"))
        response = self.llm.invoke(system_prompt=system_prompt, user_prompt=history)
        try :
            state["history"] = {self.name : response}
            state["plan"] = self.planning_tool.plan
        except :
            raise "계획을 알맞은 형태로 리턴 하기 바랍니다."
        print(f"😒 state : {state}")
        return state

