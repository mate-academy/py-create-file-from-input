import sys
import os

def create_text_file():
    file_name = input("Enter the file name (without extension): ")
    file_name = file_name.strip() + ".txt"

    print("Enter the content line by line. Type 'stop' to finish.")

    content = []
    while True:
        line = input()
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w", encoding="utf-8") as file:
        file.write("\n".join(content))

    print(f"File '{file_name}' has been created successfully!")

def main():
    create_text_file()

if __name__ == "__main__":
    main()

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if "app.main" in sys.modules:
    del sys.modules["app.main"]
