def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""
    while True:
        message = input("Enter new line of content: ")
        if message == "stop":
            break
        text = f"{text}{message}\n"

    with open(f"{file_name}.txt", "w") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
