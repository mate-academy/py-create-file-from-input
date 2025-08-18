def main() -> None:
    file_name = input("Enter name of the file: ")
    text_list = []
    while True:
        txt_line = input("Enter new line of content: ")
        if txt_line.lower() == "stop":
            break

        text_list.append(txt_line)
    file_name = file_name + ".txt"
    file_content = "\n".join(text_list)

    with open(file_name, "w") as text_file:
        text_file.write(file_content)


if __name__ == "__main__":
    main()
