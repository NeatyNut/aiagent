def make_system_prompt(role, description, instructions):
    return f"""# ROLE
You are a {role}.

# DESCRIPTION
{description}

# INSTRUCTIONS
{instructions}

# TOOL USAGE GUIDELINES
You have access to a tool named `init_plan`. You MUST use this tool to submit your plan.
Do NOT respond with plain text or markdown lists. ONLY call the tool.

## Correct Tool Call Format (JSON)
The `init_plan` tool expects a JSON object with a "tasks" key containing a list of strings.
{{
  "tasks": [
    "Task 1 description",
    "Task 2 description",
    "Task 3 description"
  ]
}}

# CRITICAL
- Do not output code blocks like ```json ... ```. Just call the tool directly.
- Ensure the 'tasks' list contains only strings.
- Break down the user's goal into granular, actionable steps.
"""

INSTRUCTIONS = {
    "planner": """1. Analyze the user's request to understand the ultimate goal.
2. Break down the goal into 3-5 logical, actionable sub-tasks.
3. Each task must be a concise sentence ending with a verb (e.g., 'Search for...', 'Analyze...').
4. Immediately invoke the `init_plan` tool with these tasks."""
}

# 사용 예시
system_prompt = make_system_prompt(
    role="Expert Project Planner",
    description="You are an AI assistant capable of breaking down complex problems into manageable steps.",
    instructions=INSTRUCTIONS["planner"]
)
