import time

def run_game():
    print("🧠 Welcome to Tiny Thinkers!")
    time.sleep(1)

    challenges = [
        {"prompt": "What does 2 + 2 equal?", "answer": "4"},
        {"prompt": "What's the capital of France?", "answer": "Paris"},
        {"prompt": "What keyword defines a function in Python?", "answer": "def"}
    ]

    for challenge in challenges:
        print("\n" + challenge["prompt"])
        user_input = input("Your answer: ").strip()

        if user_input.lower() == challenge["answer"].lower():
            print("✅ Correct!")
        else:
            print(f"❌ Nope! The correct answer was: {challenge['answer']}")
        time.sleep(0.5)

    print("\n🎉 Game over! Thanks for playing Tiny Thinkers.")

# Uncomment the line below if you want this to auto-run when executing the file
# run_game()
