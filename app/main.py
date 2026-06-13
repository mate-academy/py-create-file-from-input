def main():
    # Ask for file name
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    # Ensure .txt extension
    file_name = f"{file_name}.txt"

    # Collect content lines
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    # Write to file
    with open(file_name, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f'File "{file_name}" has been created with {len(lines)} lines of content.')


if __name__ == "__main__":
    main()
