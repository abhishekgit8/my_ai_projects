import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Setting the configuration of genAi with our api key
genai.configure(api_key=api_key)

# You can use any model in google family
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])

def chatbot_response(message, _):
    """Handles the chat interaction with the Gemini API."""
    try:
        response = chat.send_message(message, stream=True)
        res=""
        for chunk in response:
            res+=chunk.text
            yield res
    except Exception as e:
        print(f"Error interacting with Gemini API: {e}")
        if "API key not valid" in str(e):
            yield "Error: Invalid API Key. Please check your GEMINI_API_KEY."
        else:
            yield f"An error occurred: {e}"
   
