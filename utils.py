import os
from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)



model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def generate(prompt):
    context_prompt = f'You are a financial advisory personnel , and I want to seek your advice on a certain matter. Here it goes...{prompt}.Please be concise.'
    response = chat.send_message(context_prompt)
    
    return response


def get_history():
    return chat.history()