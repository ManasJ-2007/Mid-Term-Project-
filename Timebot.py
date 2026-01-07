import time

queries = []

print("TimeBot started. Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    current_time = time.time()
    queries.append((user_input, current_time))

    print("Bot: Query stored with timestamp.")

    for q, t in queries:
        if current_time - t >= 600:  # 10 minutes = 600 seconds
            print("\n--- QUIZ TIME ---")
            print("Bot: 10 minutes ago you asked:")
            print(f"'{q}'")
            print("Bot: Briefly explain what this query was about.")

            input("Your answer: ")

            queries.remove((q, t))
            print("--- Quiz completed ---\n")
            break
