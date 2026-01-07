print("Simple Chatbot started. Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break
    elif "hello" in user_input.lower():
        print("Bot: Hello! How can I help you?")
    elif "how are you" in user_input.lower():
        print("Bot: I'm functioning as expected 😄")
    else:
        print("Bot: I am still learning. Please try something else.")
