def main() -> None:
    file_name = input("Enter name of the file: ")
    text_line = input("Enter new line of content: ")
    content = []
    while text_line != "stop":
        content.append(text_line)
        print(content)
        text_line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
