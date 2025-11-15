from typing import TypedDict, Annotated, Optional, Dict, List
from state_method import update_agent_state

class Agent_State(TypedDict):
    plan: Dict[int, List]
    history: Annotated[List[Dict[str, str]], update_agent_state]


