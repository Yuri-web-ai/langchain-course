from fastapi import FastAPI
from langchain_ollama import ChatOllama
import os

app = FastAPI()

llm = ChatOllama(model="llama3", base_url=os.getenv("OLLAMA_HOST"))

@app.get("/ask")
async def ask(question: str):
    response = llm.invoke(question)
    return {"answer": response.content}
