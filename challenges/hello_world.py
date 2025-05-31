def run():
    print("\n🧠 Challenge 1: Print 'Hello, World!'")
    print("Your task is to write a Python line that prints 'Hello, World!'")

    answer = input("Type your code here: ").strip()

    if answer == "print('Hello, World!')" or answer == 'print("Hello, World!")':
        print("✅ Correct! Well done!")
    else:
        print("❌ That's not quite right. Try again next time.")
