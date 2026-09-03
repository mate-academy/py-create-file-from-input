def main() -> None:
    file_name = input("Enter name of the file: ")
    file_lines = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        file_lines.append(content)
    with open(file_name + ".txt", "w") as file:
        for line in file_lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
