
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()
# Get the local_llm value from the environment variable
local_llm = os.getenv("LOCAL_LLM")
# local_llm = "gemma2"
llm = ChatOllama(model=local_llm, temperature=0)

def askllm(prompt) :
    response = llm.invoke(prompt)
    return response.content;
