import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def write_blog_post(topic: str, outline: str, style: str) -> str:
    prompt = f"""
You are an expert technical content writer for EZERV Forge - AI Content Creation Agent.

Topic: {topic}
Outline: {outline}
Target Style: {style}

Instructions:
- Write a high-impact, engaging post optimized for social media and LinkedIn.
- AUTOMATICALLY insert commands like `/infographics` or `/charts` on separate lines where relevant.
- Format with striking headers, clear bullet points, and relevant emojis 📊🚀
- Keep paragraphs short and highly readable.
- Include a call-to-action (CTA) and relevant hashtags at the end.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content