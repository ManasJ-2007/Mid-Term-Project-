import random

count = 0
queries = []

print("CounterBot started. Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    count += 1
    queries.append(user_input)

    print("Bot: Query received.")

    if count == 5:
        quiz_query = random.choice(queries)

        print("\n--- QUIZ TIME ---")
        print("Bot: You previously asked:")
        print(f"'{quiz_query}'")
        print("Bot: Please repeat this query exactly.")

        answer = input("Your answer: ")

        if answer == quiz_query:
            print("Bot: Correct! 🎉")
        else:
            print("Bot: Incorrect.")

        count = 0
        queries.clear()
        print("--- Counter reset ---\n")
