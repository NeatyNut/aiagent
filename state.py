from typing import TypedDict, Annotated, Optional, Dict, List
from state_method import update_agent_state

class Agent_State(TypedDict):
    role:Optional[str]
    role_description:Optional[str]
    plan: Dict[str, bool]
    history: Annotated[List[Dict], update_agent_state]


