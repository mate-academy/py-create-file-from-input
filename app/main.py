def main() -> None:
    name_file = input("Enter name of the file: ")
    text_in_file = ""
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            with open(f"{name_file}.txt", "w") as file:
                file.write(text_in_file)
                break
        text_in_file += f"{text}\n"


if __name__ == "__main__":
    main()
