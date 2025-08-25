def main() -> None:

    file_name = input("Enter name of the file: ").strip()
    file_name = file_name + ".txt"  # Ensure .txt extension


    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Write to file
    with open(file_name, "w", encoding="utf-8") as f:
        for line in content_lines:
            f.write(line + "\n")

    print(f'File "{file_name}" created successfully.')


if __name__ == "__main__":
    main()
