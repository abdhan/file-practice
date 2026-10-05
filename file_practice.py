# File Operations Practice - v0.2

print("=== FILE PRACTICE ===")
print("Testing WRITE mode")

# Write to a file
with open("output.txt", "w") as file:
    file.write("Hello from Python!\n")
    file.write("This is write mode.\n")

print("✓ Data written to output.txt")