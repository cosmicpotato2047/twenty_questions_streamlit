# After
from langchain_ollama import OllamaLLM
def get_ollama_llm(model="llama2:7b"):
    return OllamaLLM(model=model)