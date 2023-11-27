import os
import openai
import rich
import time 
# Load your API key from an environment variable or secret management service
openai.api_key = "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"


#chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

for i in range(0,100):
  
  response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Dame una palabra aletoria")

#print(chat_completion.choices[0].message)
  print(response["choices"][0]["text"])
  time.sleep(10)