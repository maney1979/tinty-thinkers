def run():
    print("\n🧠 Challenge 2: Use a variable")
    print("Your task is to create a variable named 'name' and assign it your name. Then print it.")

    answer = input("Type your code here: ").strip().lower()

    if "name=" in answer and "print(name)" in answer.replace(" ", ""):
        print("✅ Nicely done! You used a variable like a pro.")
    else:
        print("❌ Not quite right. You need to assign a variable and print it.")
