def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content_list = []
    while True:
        text_input = input("Enter new line of content: ")
        if text_input.lower() == "stop":
            break
        else:
            content_list.append(text_input)

    with open(file_name, "w") as file:
        for line in content_list:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
