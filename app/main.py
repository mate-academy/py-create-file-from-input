def main() -> None:
    # Ask for the file name
    file_name = input("Enter name of the file: ").strip()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Collect content lines
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Write content to the file
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            for line in content_lines:
                f.write(line + "\n")
        print(f'✅ File "{file_name}" created successfully.')
    except Exception as e:
        print(f"⚠️ Error creating file: {e}")


if __name__ == "__main__":
    main()
