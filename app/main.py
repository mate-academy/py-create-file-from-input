def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""
    while True:
        edit_text = input("Enter new line of content: ")
        if edit_text == "stop":
            break
        text += edit_text + "\n"
    with open(f"{file_name}.txt", "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()
