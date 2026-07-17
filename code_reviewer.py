import os
from dotenv import load_dotenv
from openai import OpenAI
from prompt import SYSTEM_PROMPT

load_dotenv()
client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
def review_code(code):
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages =[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role" :"user",
                "content":code
            }
        ],
        temperature=0.2,

    )
    return response.choices[0].message.content