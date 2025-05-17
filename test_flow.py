# LLM 인스턴스 생성 파트
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

if "GOOGLE_API_KEY" not in os.environ:
    load_dotenv()
    if "GOOGLE_API_KEY" not in os.environ:
        raise "Make file .env which contains GOOGLE_API_KEY"

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0, max_retries=3)

# langchain 활용

from langchain_core.prompts import ChatPromptTemplate


# prompt = ChatPromptTemplate.from_messages([
#     (
#         "system",
#         "{progress}"
#     ),
#     ("human", "{input}")
# ])

# human_input = input("question : ")

# chain = prompt | llm

# response = chain.invoke(
#     {
#         "progress": "You are helpful assistant that gets purpose of human's input and send the purpose to another assistant for making process",
#         "input" : human_input
#     }

# )

# print(response)

# aiagent 활용

from langchain.agents import initialize_agent, load_tools, AgentType

tools = load_tools(["llm-math"], llm=llm)
