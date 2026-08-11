from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, MODEL_NAME

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME,
    temperature=0.5
)

def edit_article(topic: str, draft: str) -> str:
    """Edits, polishes, and improves the drafted blog post."""
    prompt = (
        f"You are a senior editor. Review and polish the following blog post on '{topic}'.\n\n"
        f"Draft:\n{draft}\n\n"
        "Tasks:\n"
        "1. Fix any grammatical or phrasing issues.\n"
        "2. Make the tone engaging and professional.\n"
        "3. Add a catchy main title (# Title) and a short 'Key Takeaways' section at the end.\n"
        "Return the final edited article in Markdown."
    )
    response = llm.invoke(prompt)
    return response.content