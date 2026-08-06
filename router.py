import openai_client
import gemini_client

def ask(prompt):

    try:
        print("+-------------+ Using OpenAI +-------------+")
        return openai_client.ask(prompt)
    except Exception as e:
        print("Failed: ", e)

    try: 
        print("+-------------+ Using Gemini +-------------+")
        return gemini_client.ask(prompt)
    except Exception as e:
        print("Failed: ", e)

    return "No AI providers are available."
    