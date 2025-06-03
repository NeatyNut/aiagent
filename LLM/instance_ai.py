import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

class get_aiagent:

    def __init__(self): 
        load_dotenv()
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)