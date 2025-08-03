from typing import List
import json

# state로 변경해야함
def init_plan(tasks:List[str]):
    """
    Description: paln을 작성합니다.
    
    Args:
        tasks (List[str]): 진행할 예정인 task list

    Return:
        plan (Dict[int, List[Any]])
    Example:
        init_plan(["구글에서 자료 검색하기", "보고서 형식으로 정리하기", "보고서를 기반으로 PPT 작성하기"]):
                {}
                ==> {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["보고서를 기반으로 PPT 작성하기", False]}
    """
    plan = {idx+1:task for idx, task in enumerate(tasks)}
    return plan
        
def add_plan(plan, task:str):
    """
    Description: plan에 task를 추가 합니다.

    Args:
        task (str): 추가할 플랜
    
    Return:
        plan (Dict[int, List[Any]])
        
    Example:
        add_plan("PPT 오타 점검하기"):
            {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["보고서를 기반으로 PPT 작성하기", False]},    
                ==> {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["보고서를 기반으로 PPT 작성하기", False], 4:["PPT 오타 점검하기", False]}
    """

    task_number = max(plan.keys())
    plan[task_number+1] = [task, False]

def delete_plan(plan, task_number:int):
    """
    Description: task_number를 통해 task를 삭제합니다.

    Args:
        task_number (int): 삭제할 task의 task_number
    
    Return:
        plan (Dict[int, List[Any]])

    Example:
        delete_plan(3):
            {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["보고서를 기반으로 PPT 작성하기", False], 4:["PPT 오타 점검하기", False]}
                ==> {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["PPT 오타 점검하기", False]}
    """

    del plan[task_number]
    max_task_number = max(plan.keys())

    for idx in range(task_number+1, max_task_number+1):
        plan[idx-1] = plan[idx]

    del plan[max_task_number]

def get_plan_dict(plan):
    """
    Description: 현재 plan을 확인합니다.

    Args:
        plan (Dict[int, List[Any]])

    Returns:
        plan_str (str) : string화 된 plan
    """
    plan_str = json.dumps(plan, indent=4, ensure_ascii=False)
    return plan_str
