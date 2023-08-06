def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    text_lines_input = []
    while True:
        line_input = input("Enter new line of content: ")
        if line_input == "stop":
            break

        text_lines_input.append(line_input + "\n")

    with open(file_name, "w") as f:
        f.writelines(text_lines_input)


if __name__ == "__main__":
    main()
