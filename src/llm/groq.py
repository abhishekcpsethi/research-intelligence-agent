from src.tools.paper_search import search_research_papers
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import SecretStr
import os

load_dotenv()


def create_chat_groq() -> ChatGroq:
    groq_key = SecretStr(os.getenv("GROQ_API_KEY") or "")
    groq = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.0,
        max_retries=2,
        api_key=groq_key,
    )
    return groq

