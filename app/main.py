def main() -> None:
    name_of_file = input("Enter name of the file: ")
    text_of_lines = []
    while True:
        text_of_line = input("Enter new line of content: ")
        if text_of_line != "stop":
            text_of_lines.append(text_of_line)
        else:
            break
    with open(f"{name_of_file}.txt", "w") as f:
        for line in text_of_lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
