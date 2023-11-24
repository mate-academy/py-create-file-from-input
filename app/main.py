def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            break
        content.append(content_line)

    with open(f"{file_name}.txt", "a") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
