import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()


def generate_outline(topic: str) -> str:
    """
    AI Planner Agent: Generates a blog/content outline using the Groq API.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing! Make sure it is set in your .env file or secrets.")

    client = Groq(api_key=api_key)

    prompt = f"""
You are an expert AI content planner and strategist.
Create a comprehensive, high-quality content outline for the following topic:

Topic: {topic}

Structure your output as follows:
1. 🎯 Catchy Title Options (3 suggestions)
2. 📌 Target Audience & Core Value
3. 💡 Introduction Hook & Key Takeaways
4. 🛠️ Main Sections (with sub-points and key details)
5. 🏁 Conclusion & Call-to-Action
"""

    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a professional AI content planning agent."},
            {"role": "user", "content": prompt}
        ],
        model="openai/gpt-oss-20b"
    )

    return response.choices[0].message.content