def main() -> None:
    file_name = input("Enter name of the file: ").strip()

    if not file_name:
        print("File name cannot be empty!")
        return

    file_name += ".txt"  # Append .txt extension

    print("Enter the content line by line. Type 'stop' to finish.")
    content_lines = []

    while True:
        line = input("Enter new line of content: ").strip()
        if line.lower() == "stop":
            break
        content_lines.append(line)

    try:
        with open(file_name, "w") as file:
            file.write("\n".join(content_lines))
        print(f"File '{file_name}' has been created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


if __name__ == "__main__":
    main()
