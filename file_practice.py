# File Operations Practice - v1.0

print("=== FILE OPERATIONS PRACTICE ===")
print("1. Write mode (overwrites)")
print("2. Append mode (adds to end)")
print("3. Read mode (display file)")

choice = input("\nChoose mode (1-3): ")

if choice == "1":
    text = input("Enter text to write: ")
    with open("test_output.txt", "w") as file:
        file.write(text + "\n")
    print("✓ File written (overwrites old content)")

elif choice == "2":
    text = input("Enter text to append: ")
    with open("test_output.txt", "a") as file:
        file.write(text + "\n")
    print("✓ Text appended (keeps old content)")

elif choice == "3":
    try:
        with open("test_output.txt", "r") as file:
            content = file.read()
        print("\n--- FILE CONTENTS ---")
        print(content)
    except FileNotFoundError:
        print("No file found yet! Use option 1 or 2 first.")

else:
    print("Invalid choice!")