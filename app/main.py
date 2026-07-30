def main() -> None:
    file_name = input("Enter name of the file: ")

    text = []
    while True:
        text_line = input("Enter new line of content: ")
        if text_line == "stop":
            break
        text.append(f"{text_line}\n")

    text = "".join(text)
    with open(f"{file_name}.txt", "w") as file:
        file.write(text)


if __name__ == "__main__":
    main()
