def formatMessages(messages):

    formatted = ""

    for message in messages:

        role = message["role"]
        content = message["content"]

        if role == "user":
            formatted += f"User: {content}\n"

        elif role == "assistant":
            formatted += f"Assistant: {content}\n"


    return formatted