import json
import os

memoryPath = "Memory/temp.json"


def loadMemory():

    os.makedirs("Memory", exist_ok=True)

    if not os.path.exists(memoryPath):
        return []

    with open(memoryPath, "r") as file:
        return json.load(file)


def saveMemory(messages):

    os.makedirs("Memory", exist_ok=True)

    with open(memoryPath, "w") as file:
        json.dump(
            messages,
            file,
            indent=4
        )