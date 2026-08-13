import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def write_blog_post(topic: str, outline: str, style: str) -> str:
    """
    Generates a social media or LinkedIn-styled blog post using Groq based on the outline and style.
    """
    prompt = f"""
    You are an expert technical content writer specializing in viral LinkedIn and social media posts.
    
    Topic: {topic}
    Outline: {outline}
    Target Style: {style}
    
    Instructions:
    - Write a high-impact, engaging post optimized for LinkedIn or tech social networks.
    - Format it with striking headers, clear bullet points, and relevant emojis 📊🚀💡 to simulate infographics and visual data breakdown.
    - Keep paragraphs short, punchy, and readable on mobile devices.
    - Include a strong call-to-action (CTA) and relevant hashtags at the end.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content