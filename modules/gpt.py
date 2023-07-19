import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("open_api_key")

def getResponse(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content