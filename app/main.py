def main() -> None:
    file_name = get_file_name()

    content = get_file_content()

    create_file(file_name, content)


def get_file_name() -> str:
    """Get and validate file name."""
    while True:
        file_name = input("Enter name of the file: ").strip()
        if file_name:  # Check not empty
            return file_name


def get_file_content() -> list:
    """Get content line by line until 'stop'."""
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        content.append(line)
    return content


def create_file(file_name: str, content: list) -> bool:
    """Create .txt file with content."""
    full_name = f"{file_name}.txt"
    with open(full_name, "w") as f:
        for line in content:
            f.write(line + "\n")
    return True


if __name__ == "__main__":
    main()
