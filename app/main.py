def create_file_from_input() -> None:
    file_name = input("Enter name of the file: ")

    full_name = f"{file_name}.txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")

        if line.lower() == "stop":
            break

        content_lines.append(line)

    with open(full_name, "w") as file:
        file.write("\n".join(content_lines))


def main() -> None:
    create_file_from_input()


if __name__ == "__main__":
    main()
