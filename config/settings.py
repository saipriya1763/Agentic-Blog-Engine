import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Retrieve API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found! Please check your .env file.")

# Default model configuration
MODEL_NAME = "llama-3.3-70b-versatile"