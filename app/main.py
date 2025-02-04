from typing import Any


def main() -> Any:
    file_name = input("Enter name of the file: ") + ".txt"
    content_lines = []

    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        content_lines.append(content)

    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))

if __name__ == "__main__":
    main()
