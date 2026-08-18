import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def review_blog_post(draft: str) -> str:
    """
    Reviews, polishes, and finalizes the blog post draft for maximum social media impact.
    """
    prompt = f"""
    You are an expert Chief Editor. Review and polish the following blog post draft to make it completely ready for social media publication.
    
    Draft:
    {draft}
    
    Instructions:
    - Ensure the tone is engaging, professional yet catchy.
    - Verify that the layout includes emojis, clear formatting, headers, and bullet points.
    - Polish any awkward phrasing while maintaining the core message.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    
    return response.choices[0].message.content