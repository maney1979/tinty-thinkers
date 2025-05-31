def run():
    print("\n🧠 Challenge 6: Use a loop to print items in a list")
    print("Write a list of fruits and use a for-loop to print each one.")

    answer = input("Type your code here: ").strip().lower()

    if "fruits" in answer and "[" in answer and "]" in answer and "for" in answer and "in" in answer and "print" in answer:
        print("✅ That’s it! You looped through a list.")
    else:
        print("❌ Try again. You need to define a list and print each item using a for-loop.")
