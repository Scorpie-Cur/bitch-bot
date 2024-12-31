# Prerequisites 
It's important to setup a proper discord bot token. I highly recommend looking at discords documentation for their documentation on their services. https://discord.com/developers/docs/quick-start/getting-started

Next it's important to install the discord python library,  run the following command to install discord.py

```shell
pip install discord.py
```


# Parsing the ollama response.

```json
{
    "model": "{Modelname}",
    "created_at": "{TimeStamp}",
    "message": {
        "role": "assistant",
        "content": "Response From LLM"
    },
    "done_reason": "stop",
    "done": true,
    "total_duration": ,
    "load_duration": ,
    "prompt_eval_count": ,
    "prompt_eval_duration": ,
    "eval_count": ,
    "eval_duration": 
}
```
Sample of the json response object that the ollama will return.

```python
response = requests.post(ollama_API, headers=headers, data=json.dumps(data))
    response_json = response.json()
    model_message = response_json["message"]["content"]
```
Parsing out the message content


# Limitation
Since discord has a limit of 2000 characters, I highly recommend wrapping the prompt area of the model data with the following. 

```json
data = {
    "model": active_model,
    "messages": [
        {
        "role": "user",
        "content": "Keep your response short for the user, here is the users message. '" + prompt + "'"
        }
    ],
    "stream": False
}
```

The LLM follows the command very well and will provide short answers in the message to the user.
