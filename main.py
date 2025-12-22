from unittest import result
from dotenv import load_dotenv
load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults  # правильный импорт
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

# Правильный инструмент (TavilySearchResults, а не TavilySearch)
tools = [TavilySearchResults(max_results=3)]

llm = ChatOpenAI(model="gpt-4o", temperature=0)
react_prompt = hub.pull("hwchase17/react")  # всё ок
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input", "agent_scratchpad", "tool_names", "tools"]
).partial(format_instructions=output_parser.get_format_instructions())

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt_with_format_instructions
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,  handle_parsing_errors=True)
extract_output = RunnableLambda(lambda x: x["output"])
parse_output = RunnableLambda(lambda x: output_parser.parse(x))

chain = agent_executor | extract_output | parse_output

def main():
    result = chain.invoke(
        {"input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"}
    )
    print(result.answer)
    print(result.sources)

if __name__ == "__main__":
    main()