from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text


console = Console()


def cleanResponse(response):

    if response is None:
        return ""

    response = response.strip()

    while "\n\n\n" in response:
        response = response.replace("\n\n\n", "\n\n")

    return response


def showResponse(response):

    response = cleanResponse(response)

    console.print()

    console.print(
        Panel(
            Markdown(response),
            title="Mystique",
            expand=False
        )
    )

    console.print()
    

def showUserMessage(message):

    console.print()

    console.print(
        Text(
            f"You: {message}",
            style="bold cyan"
        )
    )


def showSystemMessage(message):

    console.print(
        Text(
            message,
            style="bold yellow"
        )
    )