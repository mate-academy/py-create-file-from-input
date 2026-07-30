def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    content = input("Enter new line of content: ")
    list_of_content = []
    while content != "stop":
        list_of_content.append(content)
        content = input("Enter new line of content: ")
    with open(filename, "w") as file:
        for line in list_of_content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
