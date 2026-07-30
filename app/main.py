def main() -> None:
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []

    while True:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            break
        content_lines.append(content)

    with open(file_name, "w") as output_file:
        output_file.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
