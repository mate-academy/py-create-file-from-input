import os


def main() -> None:
    file_name = input("Enter name of the file: ")
    full_file_name = f"{file_name}.txt"

    if os.path.exists(full_file_name):
        confirm = input(
            f"The file '{full_file_name}' already exists. "
            f"Do you want to overwrite it? (yes/no): "
        )
        if confirm.lower() != "yes":
            print("Operation cancelled.")
            return

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    total_words = sum(len(line.split()) for line in lines)
    total_chars = sum(len(line) for line in lines)

    with open(full_file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")

    print(f'✅ File "{full_file_name}" created successfully.')
    print(
        f'📌 Total lines: {len(lines)} | Words: {total_words} | '
        f'Characters: {total_chars}'
    )


if __name__ == "__main__":
    main()
