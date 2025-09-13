from tools import init_plan, add_plan, delete_plan, get_plan_dict
from system_prompt import *
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from state import Agent_State
from state_method import update_agent_state
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import json

class Planner_Agent:
    def __init__(self):
        load_dotenv()
        self.name = "planner"
        self.tools = [init_plan, add_plan, delete_plan]
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
        self.llm = llm.bind_tools(self.tools)

    def generate(self, state:Agent_State):
        system_prompt = make_system_prompts(self.name, role_prompts.get(self.name), system_prompts.get(self.name))
        
        # Use a list of tuples for more robust message construction
        messages = [
            ("system", system_prompt)
        ]
        # Convert history to the message format
        for message in state['history']:
            if 'user' in message:
                user_content = message['user']
                # DIAGNOSTIC: Replace empty user content to test hypothesis
                if not user_content or not user_content.strip():
                    user_content = "(No input provided)"
                messages.append(("human", user_content))
            if 'planner' in message:
                # The content from the previous turn is an AIMessage object
                if hasattr(message['planner'], 'content'):
                    messages.append(("ai", message['planner'].content))
                else:
                    messages.append(("ai", str(message['planner'])))

        response = self.llm.invoke(messages)
        
        update_agent_state(state, {self.name:response})
        state["plan"] = get_plan_dict(state["plan"])

        print(f"😒 state : {state}")
        return {"plan": state["plan"]}

