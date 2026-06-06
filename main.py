from dotenv import load_dotenv
load_dotenv()
from tavily import TavilyClient #taily real time websearch ker raha hota hai
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage


import os

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))



@tool
def surfInternet(query: str): # jab tool create kerte hamko docstring 2 coma ander likhte jaruri hota hAI
  """Use this tool from getting latest information from the internet"""
  result = tavily_client.search(query=query)
  return  result["results"] #tavily_client.search() dictionary return karta hai, object nahi.

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(model=model, tools=[surfInternet])

response = agent.invoke({
  'messages': [HumanMessage(content="Who is cm of west bengal?")]
})
print(response['messages'][-1].text)