def run():
    print("\n🧠 Challenge 4: Write a for-loop")
    print("Write code that uses a for-loop to print numbers from 1 to 5.")

    answer = input("Type your code here: ").strip().lower()

    if "for" in answer and "in" in answer and "print" in answer and "range" in answer:
        print("✅ Nice! You used a for-loop.")
    else:
        print("❌ Not quite. Try using: for i in range(1, 6): print(i)")
