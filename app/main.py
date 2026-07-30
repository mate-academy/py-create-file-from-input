def get_file_name() -> str:
    file_name = input("Enter name of the file: ").strip()
    return f"{file_name}.txt"


def get_file_content() -> list[str]:
    lines = []

    while True:
        line = input("Enter new line of content: ")

        if line.lower() == "stop":
            break

        lines.append(line)

    return lines


def write_to_file(file_name: str, lines: list[str]) -> None:
    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(f"{line}\n")


def main() -> None:
    file_name = get_file_name()
    content = get_file_content()
    write_to_file(file_name, content)

    print(f'File "{file_name}" created successfully!')


if __name__ == "__main__":
    main()
