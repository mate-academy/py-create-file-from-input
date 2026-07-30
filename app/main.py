def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        content_lines.append(new_line)

    with open(f"{file_name}.txt", "w") as output_file:
        output_file.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
