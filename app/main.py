def main() -> None:
    # Prompt the user for the file name
    file_name = input("Enter name of the file: ")

    # Add .txt extension if not provided
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")

        if line.strip().lower() == "stop":
            break

        content_lines.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
