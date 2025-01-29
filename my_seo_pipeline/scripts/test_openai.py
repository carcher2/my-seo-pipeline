import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in your .env file!")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Make a chat request
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello, OpenAI!"}]
)

# Print response
print(response.choices[0].message.content)