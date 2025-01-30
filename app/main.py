def main() -> None:
    """Creates a text file with user-provided content."""
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("Error: File name cannot be empty.")
        return

    file_name += ".txt"
    content_lines = []

    while True:
        line = input("Enter new line of content: ").strip()
        if line.lower() == "stop":
            break
        content_lines.append(line)

    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("\n".join(content_lines))
        print(f'File "{file_name}" has been created successfully.')
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
