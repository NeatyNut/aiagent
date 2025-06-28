import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent 
from dotenv import load_dotenv
from typing import List

class Agent:

    def __init__(self, tools:List): 
        load_dotenv()
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
        self.agent = create_react_agent(model=self.llm)