import router

while True:

    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    response = router.ask(prompt)

    print(response)