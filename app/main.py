def main() -> None:
    """
    Main function to collect filename and content,
    then write to a .txt file.
    """
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    file_name_with_extension = f"{file_name}.txt"
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    try:
        with open(file_name_with_extension, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
        print(f'File "{file_name_with_extension}" created successfully.')
    except OSError as error:
        print(f"Error creating file: {error}")


if __name__ == "__main__":
    main()
