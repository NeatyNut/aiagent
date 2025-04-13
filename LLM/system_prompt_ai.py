from langchain_core.prompts import ChatPromptTemplate

class set_role:
    
    def __call__(role):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful assistant to get korean University URL by using naver.",
                ),
                ("human", "{school_name}"),
            ]
        )

        return prompt