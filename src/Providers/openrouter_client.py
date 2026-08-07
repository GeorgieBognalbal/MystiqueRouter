from openrouter import OpenRouter
import os

client = OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY")
    )

def ask(prompt):
    response = client.chat.send(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content