def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    text_list = []

    while True:
        text = input("Enter new line of content: ")
        if text.lower() == "stop":
            break
        text_list.append(text)

    with open(file_name, "a") as text_file:
        for line in text_list:
            text_file.write(line + "\n")


if __name__ == "__main__":
    main()
