from langchain_core.messages import HumanMessage , AIMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph , END , START
from typing import TypedDict , List , Union
from dotenv import load_dotenv
import os


load_dotenv()

class AgentState(TypedDict):
    messages : List[Union[HumanMessage ,AIMessage]]


llm = ChatGroq(model="llama-3.1-8b-instant",
                   groq_api_key=os.getenv("GROQ_API_KEY")
                   )



def AgentBot(state :AgentState):
    
    response = llm.invoke(state["messages"])

    state["messages"].append(AIMessage(content=response.content))
    print(response.content)


    return state






graph = StateGraph(AgentState)

graph.add_node("chatbot", AgentBot)
graph.add_edge(START , "chatbot")
graph.add_edge("chatbot" , END) 

agent = graph.compile()


conversation_history = []

userinput = input("You: ")

while userinput != "exit":
    conversation_history.append(HumanMessage(content=userinput))
    result = agent.invoke({"messages": conversation_history})
    conversation_history = result["messages"]
    userinput = input("You: ")