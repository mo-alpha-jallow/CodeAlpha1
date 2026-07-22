def chatbot():

    responses = {
        "hello": "Hello! How can I help you?",
        "how are you": "I am doing great. Thanks for asking!",
        "what is your name": "I am CodeAlpha's Basic Chatbot.",
        "thanks": "You're welcome!",
        "good morning": "Good morning! Have a wonderful day!",
        "good night": "Good night! Sleep well!",
        "help": "You can ask me about my name or greet me."
    }

    print("================================")
    print("       BASIC CHATBOT")
    print("================================")
    print("Hello! I am your chatbot.")

    while True:

        user_message = input("You: ").lower()

        if user_message == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        elif user_message in responses:
            print(f"Bot: {responses[user_message]}")

        else:
            print("Bot: Sorry, I don't understand.")


chatbot()