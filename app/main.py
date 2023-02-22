def main() -> None:
    content = []
    file_name = input("Enter name of the file: ")
    while True:
        line_content = input("Enter new line of content: ")
        if line_content == "stop":
            write_to_file(file_name, content)
            break
        content.append(line_content)


def write_to_file(file_name: str, content: list[str]) -> None:
    with open(file_name + ".txt", "a") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
