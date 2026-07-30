def main() -> None:
    file_name_input = input("Enter name of the file: ").strip()
    if not file_name_input.lower().endswith(".txt"):
        file_name_input += ".txt"

    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break

        content_lines.append(line)

    with open(file_name_input, "w") as file:
        file.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
