def main() -> None:
    file_name = input("Enter name of the file: ")
    file_contents = []
    content_line = input("Enter new line of content: ")

    while content_line != "stop":
        file_contents.append(content_line)
        content_line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as file:
        for content in file_contents:
            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
