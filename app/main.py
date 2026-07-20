def main() -> None:
    file_name = input("Enter name of the file: ").strip()

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break

        content_lines.append(line)

    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write("\n".join(content_lines))
        print(f"\n# File '{file_name}' was successfully created!")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


if __name__ == "__main__":
    main()
