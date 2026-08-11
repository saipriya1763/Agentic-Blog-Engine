from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME,
    temperature=0.7
)

def write_article(topic: str, outline: str) -> str:
    """Drafts a full blog post based on the provided outline."""
    prompt = (
        f"You are a professional tech writer. Using the following outline, write a complete, engaging blog post on '{topic}':\n\n"
        f"Outline:\n{outline}\n\n"
        "Format the output neatly in Markdown with headings."
    )
    response = llm.invoke(prompt)
    return response.content