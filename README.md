# Mystique v1 — Prerequisites & Setup

## Prerequisites

Before running Mystique, make sure you have:

* **Python 3.x**
* **pip**
* An **OpenAI API key**
* A **Google Gemini API key**

## Python Packages

Mystique currently uses these packages:

```bash
pip install openai
pip install google-genai
pip install python-dotenv
```

Or install everything at once:

```bash
pip install openai google-genai python-dotenv
```

### Packages

| Package         | Purpose                                      |
| --------------- | -------------------------------------------- |
| `openai`        | Connects Mystique to OpenAI models           |
| `google-genai`  | Connects Mystique to Google Gemini models    |
| `python-dotenv` | Loads API keys and configuration from `.env` |

## Environment Variables

Create a `.env` file in the root of the project:

```env
OPENAI_API_KEY="your_openai_api_key"
GEMINI_API_KEY="your_gemini_api_key"
```

## Current Architecture

```text
                 Mystique
                    |
                    v
                  Router
                 /      \
                /        \
           OpenAI       Gemini
```

Mystique currently attempts to use OpenAI first. If the request fails, the router falls back to Gemini.

## Current Python Structure

```text
Mystique/
│
├── main.py
├── router.py
├── openai_client.py
├── gemini_client.py
├── .env
├── .gitignore
└── requirements.txt
```

## requirements.txt

The current dependencies can also be stored in:

```text
openai
google-genai
python-dotenv
```

Then install them with:

```bash
pip install -r requirements.txt
```

## Current Status

**Mystique is currently a side project / proof of concept.**

The first version focuses on establishing the core idea:

> One interface for multiple AI providers with automatic fallback.

Future versions may introduce additional providers, smarter routing, conversation memory, local AI models, an API layer, and other capabilities.
