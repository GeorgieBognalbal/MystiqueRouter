import src.router as router
from src.Memory import memoryManager as memory
from src.Utils import responseFormatter
from src.Utils import terminal
from rich.prompt import Prompt

messages = memory.loadMemory()

while True:

    prompt = Prompt.ask(
    "[bold cyan]You ❯[/bold cyan]"
)
    
    if prompt.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    stop_event, thread = terminal.start_thinking()

    response = router.ask(messages)

    stop_event.set()
    thread.join()

    print("\r" + " " * 120 + "\r", end="")

    messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    responseFormatter.showResponse(response)

    memory.saveMemory(messages)