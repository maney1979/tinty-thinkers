# main.py
import time
from challenges import hello_world, variables, if_statements, loops, functions
from database import save_score  # <-- optional Supabase call

def main():
    print("🧠 Welcome to Tiny Thinkers!")
    print("Type 'start' to begin or 'quit' to exit.")

    while True:
        command = input(">>> ").strip().lower()

        if command == 'start':
            print("🚀 Starting your first challenge...")
            time.sleep(1)

            print("Choose a challenge:")
            print("1 = Hello World")
            print("2 = Variables")
            print("3 = If Statements")
            print("4 = Loops")
            print("5 = Functions")

            choice = input("Enter 1, 2, 3, 4, or 5: ").strip()

            if choice == "1":
                hello_world.run()
            elif choice == "2":
                variables.run()
            elif choice == "3":
                if_statements.run()
            elif choice == "4":
                loops.run()
            elif choice == "5":
                functions.run()
            else:
                print("❌ Invalid choice. Starting over...")
        elif command == 'quit':
            print("👋 Goodbye, thinker!")
            break
        else:
            print("🤖 Unknown command. Type 'start' or 'quit'.")

if __name__ == "__main__":
    main()
