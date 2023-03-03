def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []
    content_line = input("Enter new line of content: ")

    while content_line != "stop":
        file_content.append(content_line + "\n")
        content_line = input("Enter new line of content: ")

    with open(file_name + ".txt", "w") as f:
        f.writelines(file_content)


if __name__ == "__main__":
    main()
