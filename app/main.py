def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content_list = []
    while True:
        file_content = input("Enter new line of content: ")
        if file_content.strip().lower() == "stop":
            break
        file_content_list.append(file_content)

    with open(f"{file_name}.txt", "a") as file:
        for content in file_content_list:
            file.write(content + "\n")


if __name__ == "__main__":
    main()
