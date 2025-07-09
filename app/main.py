def main() -> None:
    file_name = input("Enter name of the file: ").strip() + ".txt"
    content_lines = []

    while True:
        line = input("Enter new line of content: ").strip()
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(file_name, "w", encoding="utf-8") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"File '{file_name}' has been created.")


if __name__ == "__main__":
    main()
