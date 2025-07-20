from typing import List
import json

class planner_tool:
    
    def __init__(self):
        self.plan = {}

    def init_plan(self, tasks:List[str]):
        """
        Description: paln을 작성합니다.
        
        Args:
            tasks (List[str]): 진행할 예정인 task list

        Example:
            init_plan(["구글에서 자료 검색하기", "보고서 형식으로 정리하기", "보고서를 기반으로 PPT 작성하기"]):
                    {}
                    ==> {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["보고서를 기반으로 PPT 작성하기", False]}
        """
        self.plan = {idx+1:task for idx, task in enumerate(tasks)}
            
    def add_plan(self, task:str):
        """
        Description: plan에 task를 추가 합니다.

        Args:
            task (str): 추가할 플랜
        
        Example:
            add_plan("PPT 오타 점검하기"):
                {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["보고서를 기반으로 PPT 작성하기", False]},    
                    ==> {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["보고서를 기반으로 PPT 작성하기", False], 4:["PPT 오타 점검하기", False]}
        """

        task_number = max(self.plan.keys())
        self.plan[task_number+1] = [task, False]

    def delete_plan(self, task_number:int):
        """
        Description: task_number를 통해 task를 삭제합니다.

        Args:
            task_number (int): 삭제할 task의 task_number
        
        Example:
            delete_plan(3):
                {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["보고서를 기반으로 PPT 작성하기", False], 4:["PPT 오타 점검하기", False]}
                    ==> {1:["구글에서 자료 검색하기", False], 2:["보고서 형식으로 정리하기", False], 3:["PPT 오타 점검하기", False]}
        """

        del self.plan[task_number]
        max_task_number = max(self.plan.keys())

        for idx in range(task_number+1, max_task_number+1):
            self.plan[idx-1] = self.plan[idx]

        del self.plan[max_task_number]

    def get_plan_dict(self):
        """
        Description: 현재 plan을 확인합니다.

        No Args

        Returns:
            str: plan_str
        """
        plan_str = json.dumps(self.plan, indent=4, ensure_ascii=False)
        return plan_str
