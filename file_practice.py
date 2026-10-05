# File Operations Practice - v0.3

print("=== FILE PRACTICE ===")

# First, write some data
print("1. Testing WRITE mode")
with open("output.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("This is line 2.\n")
print("✓ Data written")

# Now read it back
print("\n2. Testing READ mode")
with open("output.txt", "r") as file:
    content = file.read()

print("File contents:")
print(content)