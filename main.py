from langgraph.graph import StateGraph, START, END
from state import AgentState
from agents import PlannerAgent

graph_builder = StateGraph(AgentState)
planner = PlannerAgent()
graph_builder.add_node("planner", planner.generate)
graph_builder.add_edge(START, "planner")
graph_builder.add_edge("planner", END)

graph_builder.set_entry_point("planner")

app = graph_builder.compile()
state = AgentState()
result = app.invoke(state)

print(f"🥳 최종 결과물 >>\n{result}")