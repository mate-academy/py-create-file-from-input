def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    file_name += ".txt"

    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(content_lines))

    print(f"File '{file_name}' has been created with your content.")


if __name__ == "__main__":
    main()
