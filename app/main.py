def main() -> None:
    name_file = input("Enter name of the file: ") + ".txt"
    content = []
    while True:
        text_file = input("Enter new line of content: ")
        if text_file.lower() == "stop":
            break
        content.append(text_file)

    with open(name_file, "a") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
