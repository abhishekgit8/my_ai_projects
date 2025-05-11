#Create a python environment and activate it
python -m venv env
pip install -r requirements.txt

#Create a google api key for the agent
#For api key -> https://aistudio.google.com/app/apikey

#After setting the API Key in the .env file and importing it in the agent.py to generate the response in the chatbot_response().
#Call the chatbot_response() in the app.py to set with the gradio thereto set the Simple better UI for the bot.

# Run the chatbot by:-> gradio app.py
