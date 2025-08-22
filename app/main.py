def main() -> None:
    # Ask user for the file name
    file_name = input("Enter name of the file: ")

    # Add .txt extension if not already present
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # List to store content lines
    lines = []

    # Ask for lines until user types 'stop'
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    # Write content to the file
    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    print(f'File "{file_name}" created successfully.')


if __name__ == "__main__":
    main()
