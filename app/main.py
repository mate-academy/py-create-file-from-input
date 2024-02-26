def main() -> None:
    text = ""
    text_list = []
    file_name = input("Enter name of the file: ")
    while text != "stop":
        text = input("Enter new line of content: ")
        if text != "stop":
            text_list.append(text)

    with open(file_name + ".txt", "w") as file:
        for text_line in text_list:
            file.write(text_line + "\n")


if __name__ == "__main__":
    main()
