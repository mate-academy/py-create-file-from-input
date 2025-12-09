def main() -> None:
    file_name = input("Enter name of the file: ")
    content_lines = []

    while True:
        line = input("Enter new line of content: ")

        if line == "stop":
            break
        else:
            content_lines.append(line)
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w") as file:
        full_content = "\n".join(content_lines)
        file.write(full_content)


if __name__ == "__main__":
    main()
