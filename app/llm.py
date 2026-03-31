from langchain_google_genai import ChatGoogleGenerativeAI
from core.config import GOOGLE_API_KEY, MODEL_NAME

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=0.5
)