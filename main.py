from langgraph.graph import StateGraph, START, END
from state import AgentState, init_AgentState
from agents import PlannerAgent
from langchain_core.messages import HumanMessage
from langgraph.graph import add_messages

user_input = input(f'😒시키실 업무 입력 >>> ')


graph_builder = StateGraph(AgentState)
planner = PlannerAgent()
graph_builder.add_node("planner", planner.generate)
graph_builder.add_edge(START, "planner")
graph_builder.add_edge("planner", END)

graph_builder.set_entry_point("planner")

app = graph_builder.compile()
state = AgentState()
state = init_AgentState(state)
state['messages'] = add_messages(state['messages'], HumanMessage(user_input))
result = app.invoke(state)

print(f"🥳 최종 결과물 >>\n{result}")