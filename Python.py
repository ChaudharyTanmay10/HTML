import os
import openai

openai.api_key = os.getenv("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")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
