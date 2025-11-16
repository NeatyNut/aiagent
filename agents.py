from tools import init_plan, add_plan, delete_plan, get_plan_dict
from system_prompt import *
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from state import Agent_State
from state_method import update_agent_state
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

class Planner_Agent:
    def __init__(self):
        load_dotenv()
        self.name = "planner"
        self.tools = [init_plan, add_plan, delete_plan]
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
        self.llm = llm.bind_tools(self.tools)

    def generate(self, state:Agent_State):
        system_prompt = make_system_prompts(self.name, role_prompts.get(self.name), system_prompts.get(self.name))
        
        # Use a list of tuples for more robust message construction
        messages = [
            {"system":system_prompt}
        ]

        
        for conversation in state['history']:
            messages.append(conversation)

        message_text = ""

        for message in messages:
            message_text += f"{message.keys()[0]} : {message.values()[0]}\n"

        response = self.llm.invoke(message_text)
        
        update_agent_state(state['history'], {self.name:response.content})
        print(f"😒 state : {state}")
        state["plan"] = get_plan_dict(state["plan"])

        return {"plan": state["plan"]}

