from typing import NoReturn


def main() -> NoReturn:
    # Ask the user for the file name
    file_name: str = input("Enter name of the file: ").strip()

    # Ensure the file has a .txt extension
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Collect content lines from the user
    content_lines: list[str] = []
    while True:
        line = input("Enter new line of content: ").strip()
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Write the collected content to the file
    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"File {file_name} created with provided content.")


if __name__ == "__main__":
    main()
