def main() -> None:
    file_name = input("Enter name of the file: ")
    text_to_write = ""
    while True:
        entered_text = input("Enter new line of content: ")
        if entered_text == "stop":
            break
        text_to_write += entered_text + "\n"

    with open(f"{file_name}.txt", "w") as f:
        f.write(text_to_write)


if __name__ == "__main__":
    main()
