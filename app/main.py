def main() -> None:
    file_name = input("Enter name of the file: ")

    content_lines = []

    print("Enter lines of content (type 'stop' to finish):")
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    full_file_name = file_name + ".txt"

    with open(full_file_name, "w", encoding="utf-8") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"File '{full_file_name}' has been created successfully!")


if __name__ == "__main__":
    main()
