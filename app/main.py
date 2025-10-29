def main() -> None:
    """Main function to create a text file with user input."""
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    print(f'\nFile "{file_name}" created successfully!')
    print("File content:")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
