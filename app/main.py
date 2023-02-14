def main() -> None:
    file_name = input("Enter name of the file: ")
    content = ""
    while True:
        current_content = input("Enter new line of content: ")
        if current_content == "stop":
            break
        content += current_content + "\n"

    with open(file_name + ".txt", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
