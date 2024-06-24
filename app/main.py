def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    content_list = []
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        content_list.append(content)
    with open(file_name, "w") as file:
        for content in content_list:
            file.write(content + "\n")


if __name__ == "__main__":
    main()
