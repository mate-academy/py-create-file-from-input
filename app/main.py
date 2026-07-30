def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content_lists = []

    while True:
        content_line = input("Enter new line of content: ")

        if content_line.lower() == "stop":
            break

        content_lists.append(content_line)

    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        for line in content_lists:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
