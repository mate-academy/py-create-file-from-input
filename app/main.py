def main() -> None:
    file_name = input("Enter name of the file: ")

    file_text = ""

    text_line = input("Enter new line of content: ")

    while text_line != "stop":
        file_text += (text_line + "\n")

        text_line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as file:
        file.write(file_text)


if __name__ == "__main__":
    main()
