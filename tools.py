from typing import List
from langchain_core.tools import tool
from state import AgentState
import json


@tool
def init_plan(state:AgentState, tasks:List[str]):
    """Plan을 작성합니다..."""
    plan = {idx+1:[task, False] for idx, task in enumerate(tasks)}
    state["tasks"] = plan
    return state
