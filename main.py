from dotenv import load_dotenv
load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults  # правильный импорт

# Правильный инструмент (TavilySearchResults, а не TavilySearch)
tools = [TavilySearchResults(max_results=3)]

llm = ChatOpenAI(model="gpt-4o", temperature=0)
react_prompt = hub.pull("hwchase17/react")  # всё ок

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,  handle_parsing_errors=True)
chain = agent_executor

def main():
    result = chain.invoke(
        {"input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"}
    )
    print(result["output"])  # в ReAct-агенте ответ в ключе "output"

if __name__ == "__main__":
    main()