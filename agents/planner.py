from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME,
    temperature=0.7
)

def plan_article(topic: str) -> str:
    """Generates a structured outline for the blog post based on the given topic."""
    prompt = f"You are an expert content manager. Create a detailed, structured blog outline for the topic: '{topic}'."
    response = llm.invoke(prompt)
    return response.content