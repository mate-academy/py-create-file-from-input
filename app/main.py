def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    file_contents = list()

    content_line = input("Enter new line of content: ")
    while content_line != "stop":
        file_contents.append(content_line)
        content_line = input("Enter new line of content: ")

    with open(file_name, "w") as f:
        for item in file_contents:
            f.write(f"{item}\n")


if __name__ == "__main__":
    main()
