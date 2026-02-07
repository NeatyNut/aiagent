from typing import List, Dict
from langchain_core.tools import tool
from pydantic import BaseModel, Field

# ---------------------------------------------------------
# 1. 입력 구조(Schema)를 Pydantic으로 명확하게 정의합니다.
# ---------------------------------------------------------
class InitPlanInput(BaseModel):
    tasks: List[str] = Field(
        description="실행해야 할 세부 하위 작업들의 리스트입니다. 예: ['데이터 수집', '전처리', '보고서 작성']"
    )

# ---------------------------------------------------------
# 2. @tool 데코레이터에 args_schema를 지정합니다.
# ---------------------------------------------------------
@tool(args_schema=InitPlanInput)
def init_plan(tasks: List[str]) -> Dict[int, tuple]:
    """
    사용자의 요청을 받아서, 이를 해결하기 위한 구체적인 하위 작업(Task) 리스트로 분할하여 계획을 세웁니다.
    입력받은 각 작업은 아직 완료되지 않은 상태(False)로 초기화됩니다.
    """
    # 디버깅: 실제로 리스트가 잘 들어왔는지 확인
    print(f"\n[Tool 실행됨] 입력된 작업 목록: {tasks}")
    
    return {idx + 1: (task, False) for idx, task in enumerate(tasks)}
