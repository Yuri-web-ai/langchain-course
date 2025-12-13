# main.py
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

# Загружаем .env (OPENAI_API_KEY)
load_dotenv()

def main():
    print("Hello from langchain-course!")
    
    # Текст про Илона
    information = """
    Elon Reeve Musk FRS (born June 28, 1971) is a South African-Canadian-American businessman...
    """

    # Шаблон промпта
    summary_template = """
    Given the information {information} about a person, create:
    1. A short summary
    2. Two interesting facts about them
    """

    # Создаём промпт
    prompt = PromptTemplate.from_template(summary_template)

    # — используем gpt-4o (gpt-5 НЕТ!)
    #llm = ChatOllama(temperature=0, model="gemma3:270m")
    llm = ChatOpenAI(model="gpt-4o", temperature=0)


    # Цепочка: промпт → LLM
    chain = prompt | llm

    # Запускаем
    try:
        response = chain.invoke({"information": information})
        print("\nResult:\n", response.content)
    except Exception as e:
        print("Ошибка при вызове LLM:")
        print(e)

# Запуск
if __name__ == "__main__":
    main()