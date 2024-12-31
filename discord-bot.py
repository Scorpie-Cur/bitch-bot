import discord
from discord.ext import commands
import requests
import json


# Config
BOT_TOKEN = "{BOT_TOKEN}"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

active_model = ""

# Define LLM variables
ollama_url = "{OLLAMA_URL}"
ollama_API = ollama_url+"/api/chat"
modelList_API = ollama_url+"/api/tags"
headers = {"Content-Type": "application/json"}


def ai_gen(prompt):
    global active_model
    if active_model is None:
        active_model = "llama3.2:1b"

    data = {
        "model": active_model,
        "messages": [
            {
            "role": "user",
            "content": prompt
            }
        ],
        "stream": False
    }

    # Make POST request to Ollama API
    response = requests.post(ollama_API, headers=headers, data=json.dumps(data))
    response_json = response.json()
    model_message = response_json["message"]["content"]

    if response.status_code == 200:
        return model_message
    else:
        print("Failed to send request. Status code: ", response.status_code)
        return None

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    if message.content.startswith('$prompt'):
        userMessage = message.content.replace('$prompt', '')
        await message.channel.send(ai_gen(userMessage))


client.run(BOT_TOKEN)


