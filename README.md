# Mystique v1.5

> A multi-AI routing assistant with memory, intelligent provider selection, and terminal interface customization.

---

# Overview

Mystique is a multi-AI orchestration system that routes user requests to different AI providers based on the type of task.

Mystique uses:
- Request classification
- AI provider routing
- Memory management
- Provider fallback
- Custom terminal interface

---

# Features

- Multi-AI provider support
- Automatic request classification
- Intelligent AI routing
- Provider fallback system
- Conversation memory
- Context formatting
- Rich terminal interface

---

# Architecture

```
Mystique/
│
├── src/
│   │
│   ├── Memory/
│   │   ├── memoryManager.py
│   │   └── Formatter.py
│   │
│   ├── Providers/
│   │   ├── openai_client.py
│   │   ├── gemini_client.py
│   │   ├── groq_client.py
│   │   └── openrouter_client.py
│   │
│   ├── Utils/
│   │   └── terminal.py
│   │
│   └── router.py
│   
│
├── requirements.txt
├── .env
├── README.md
└── main.py
```

---

# AI Providers

| Category | Primary | Fallback |
|---|---|---|
| Chat | Groq | OpenAI |
| Coding | OpenRouter | Groq |
| Analysis | Gemini | OpenAI |
| Writing | Gemini | Groq |

---

# Installation

Clone the repository:

```bash
git clone <repository-url>

cd Mystique
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file:

```env
OPENAI_API_KEY=

GEMINI_API_KEY=

GROQ_API_KEY=

OPENROUTER_API_KEY=
```

---

# Running Mystique

```bash
python src/main.py
```

---

# Requirements

Current dependencies:

```
openai
google-genai
groq
python-dotenv
rich
```

---

# Version History

## v1.5

Added:
- Groq integration
- OpenRouter integration
- Rich terminal interface
- Improved project architecture

---

# Status

Current Version:

```
Mystique v1.5
```

Status:

```
Active Development
```