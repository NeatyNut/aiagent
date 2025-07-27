from langgraph.graph import StateGraph, START, END
from state import Agent_State
from state_method import initialize_agent_state
from agents import Planner_Agent
import json

user_input = input(f'😒시키실 업무 입력 >> ')

state = Agent_State(initialize_agent_state(user_input))
state_key = json.dumps(state, sort_keys=True)
graph_builder = StateGraph(state_key)

planner = Planner_Agent()
graph_builder.add_node("planner", planner.generate)
graph_builder.add_edge(START, "planner")
graph_builder.add_edge("planner", END)
