def main() -> None:
    file_name = input("Enter name of the file: ")
    text_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        text_lines.append(line + "\n")

    with open(f"{file_name}.txt", "a") as text:
        for line in text_lines:
            text.write(line)


if __name__ == "__main__":
    main()
