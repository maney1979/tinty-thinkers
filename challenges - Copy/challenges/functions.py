def run():
    print("\n🧠 Challenge 5: Define and Call a Function")
    print("Write a function called greet that prints 'Hello, Thinker!' and then call it.")

    answer = input("Type your code here: ").strip().lower()

    if "def" in answer and "greet" in answer and "print" in answer and "()" in answer:
        print("✅ Boom! You created and called a function.")
    else:
        print("❌ Close, but not quite. Make sure you define greet() and call it.")
