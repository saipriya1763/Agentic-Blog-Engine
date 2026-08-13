import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_outline(topic: str) -> str:
    """
    Generates a structured outline for the given blog topic using Groq.
    """
    prompt = f"""
    You are an expert technical content planner. Create a detailed and engaging blog post outline for the following topic:
    
    Topic: {topic}
    
    Provide the outline with clear section headings and bullet points for what to cover in each section.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content