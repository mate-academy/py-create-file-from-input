def main() -> None:
    content = []
    file_name = input("Enter name of the file: ")
    while True:
        input_content = input("Enter new line of content: ")
        if input_content == "stop":
            break
        content.append(input_content)
    with open(file_name + ".txt", "a") as file:
        for line in content:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
