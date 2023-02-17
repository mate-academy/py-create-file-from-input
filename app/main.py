def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = ""

    while True:
        line_content = input("Enter new line of content: ")
        if line_content == "stop":
            break
        content += line_content + "\n"

    with open(file_name, "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
