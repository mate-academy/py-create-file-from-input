def main() -> None:
    file_name = input("Enter name of the file: ").strip()

    if file_name.endswith(".txt"):
        full_file_name = file_name
    else:
        full_file_name = f"{file_name}.txt"

    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content_lines.append(line)

    with open(full_file_name, "w") as file:
        file.write("\n".join(content_lines))


if __name__ == "__main__":
    main()
