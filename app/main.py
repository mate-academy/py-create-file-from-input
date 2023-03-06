def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    while True:
        text_line = input("Enter new line of content: ")
        with open(file_name, "a") as text_file:
            if text_line == "stop":
                break
            text_file.write(f"{text_line}\n")


if __name__ == "__main__":
    main()
