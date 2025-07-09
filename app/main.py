def main() -> None:
    filename = input("Enter name of the file: ").strip()
    if not filename:
        print("File name cannot be empty.")
        return

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    full_filename = f"{filename}.txt"

    try:
        with open(full_filename, "w", encoding="utf-8") as file:
            file.write("\n".join(content_lines))
        print(f'File "{full_filename}" created successfully.')
    except IOError as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
