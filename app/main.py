def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    text_lines = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        text_lines.append(new_line)

    with open(file_name, "w") as new_file:
        new_file.write("\n".join(text_lines))


if __name__ == "__main__":
    main()
