def main() -> None:
    name = input("Enter name of the file: ")
    content = ""

    while True:
        text = input("Enter new line of content: ")

        if text == "stop":
            break

        if not content:
            content += text
        else:
            content += "\n" + text

    file_name = name + ".txt"
    with open(file_name, "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
