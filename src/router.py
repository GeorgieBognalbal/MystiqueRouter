import src.Providers.openai_client as openai
import src.Providers.gemini_client as gemini
import src.Providers.groq_client as groq
import src.Providers.openrouter_client as openrouter

from src.Memory import Formatter as formatter

def ask(messages):

    if not messages:
        return "No messages available."

    latestPrompt = messages[-1]["content"]

    category = groq.requestClassifier(latestPrompt)
    category = category.strip().lower()

    providers = {
        "chat": [
            ("Groq", groq.ask),
            ("OpenAI", openai.ask),
            ("OpenRouter", openai.ask),
        ],

        "coding": [
            ("OpenRouter", openrouter.ask),
            ("Gemini", gemini.ask),
        ],

        "analysis": [
            ("Gemini", gemini.ask),
            ("OpenRouter", openrouter.ask),
            ("OpenAI", openai.ask),
        ],

        "writing": [
            ("Gemini", gemini.ask),
            ("Groq", groq.ask),
        ],

        "modifying": [
            ("OpenRouter", openrouter.ask),
            ("Gemini", gemini.ask),
        ],

        "formatting": [
            ("Groq", groq.ask),
            ("Gemini", gemini.ask),
        ],
    }

    if category not in providers:
        print(f"Unknown category: {category}")
        category = "chat"

    formattedMessages = formatter.formatMessages(messages)

    for name, provider in providers[category]:

        try:

            print(f" | {name} ❯ {category}")

            return provider(formattedMessages)


        except Exception as e:

            print(
                f"{name} failed: {e}"
            )

            print(
                "Trying next provider..."
            )


    return "No AI providers are available."