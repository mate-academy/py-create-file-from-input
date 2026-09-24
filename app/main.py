def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    lines = []
    text_to_append = ""
    while (text_to_append != "stop"):
        text_to_append = input("Enter new line of content: ")
        if text_to_append != "stop":
            lines.append(text_to_append)

    file_to_append = open(file_name, "+a")
    for line in lines:
        file_to_append.write(line + "\n")

    print("File File content:")
    for line in file_to_append.readlines():
        print(line)


if __name__ == "__main__":
    main()
