import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt: str) -> str:
    """
    Sends a prompt to Gemini and returns the response.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        raise Exception(f"Gemini API Error: {str(e)}")