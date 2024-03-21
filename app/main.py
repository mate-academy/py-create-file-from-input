def main() -> None:
    content: list[str] = []
    file_name = ""
    keyword_to_break_loop = "stop"

    while True:
        if not file_name:
            file_name = input("Enter name of the file: ")

        entered_content = input("Enter new line of content: ")

        if entered_content == keyword_to_break_loop:
            break

        content.append(entered_content + "\n")

    with open(f"{file_name}.txt", "w") as file:
        file.writelines(content)


if __name__ == "__main__":
    main()
