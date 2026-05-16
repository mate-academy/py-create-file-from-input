def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        content_lines.append(text)
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w") as file:
        for content in content_lines:
            file.write(content + "\n")


if __name__ == "__main__":
    main()
