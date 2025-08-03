def initialize_agent_state(user_message):
    """agent 상태를 초기화합니다.
    
    Args:
        user_message (str): 사용자의 요구사항.

    Returns:
        dict: 초기화된 agent 상태.
    """
    return {
        'plan': {},
        'history': [{'user':user_message}]  # 대화 기록을 저장하기 위한 공간
    }

def update_agent_state(agent_state, role:str, response:str):
    """state를 업데이트합니다.

    Args:
        agent_state (dict): 현재 agent 상태.
        role(str): AI의 역할.
        response (str): AI의 응답.

    Returns:
        dict: 업데이트된 agent 상태.role
    """
    agent_state['history'].append({role: response})
    return agent_state

def update_agent_plan_state(agent_state, task_number:int, tf:bool):
    """state의 plan을 업데이트합니다.

    Args:
        agent_state (dict): 현재 agent 상태.
        task(str): plan의 업무
        ai_response (str): AI의 응답.
    
    Returns:
        dict: plan상태가 업데이트된 agent 상태.
    """

    if agent_state.get("plan", {}).get(task_number, "") != "":
        agent_state["plan"][task_number][-1] = tf
    else:
        raise "agent_state에 속한 task를 제공하세요."
    
    return agent_state