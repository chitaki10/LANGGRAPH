
from langchain_core.messages import HumanMessage , AIMessage
from langchain_groq import ChatGroq


from langchain_groq import ChatGroq
from langgraph.graph import StateGraph , END , START
from typing import TypedDict , List , Union
from dotenv import load_dotenv
import os


load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant",
                   groq_api_key=os.getenv("GROQ_API_KEY")
                   )

response = llm.invoke([HumanMessage(content="What is the capital of France?")])
print(response.content)